---
schema: strategy-research-record-v1
title: "Augmented Dickey-Fuller Stationarity Filter Falsification in Walk-Forward ETF Pairs Trading"
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
  - augmented-dickey-fuller
  - stationarity-testing
  - walk-forward-analysis
  - falsification-study
  - etf
status: research-only
confidence: high
source_as_of: 2026-09-11
sources:
  - "sefaav, Does ADF filtering actually improve pairs-trading performance out-of-sample?, GitHub repository sefaav/quant-research-notebooks, commit d44ae7a332b2a35a914a27897094723730b45cfb, September 11, 2026. Stable URL: https://github.com/sefaav/quant-research-notebooks"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Augmented Dickey-Fuller Stationarity Filter Falsification in Walk-Forward ETF Pairs Trading

## Provenance

- **Primary Source:** `sefaav`, *"Does ADF filtering actually improve pairs-trading performance out-of-sample? A walk-forward experiment on 92 economically related ETF pairs, 2008–2026"*, published September 11, 2026 (`source-reported`).
  - GitHub Repository URL: [https://github.com/sefaav/quant-research-notebooks](https://github.com/sefaav/quant-research-notebooks)
  - Canonical Commit SHA: `d44ae7a332b2a35a914a27897094723730b45cfb`
  - Study Path: [`pairs_trading_stationarity`](https://github.com/sefaav/quant-research-notebooks/tree/d44ae7a332b2a35a914a27897094723730b45cfb/pairs_trading_stationarity)
  - Research Monograph / Executed Notebook: [`pairs_trading_stationarity/study.ipynb`](https://github.com/sefaav/quant-research-notebooks/blob/d44ae7a332b2a35a914a27897094723730b45cfb/pairs_trading_stationarity/study.ipynb)
  - Experiment Code Implementation: [`pairs_trading_stationarity/study_lib.py`](https://github.com/sefaav/quant-research-notebooks/blob/d44ae7a332b2a35a914a27897094723730b45cfb/pairs_trading_stationarity/study_lib.py)
  - Unit Tests: [`pairs_trading_stationarity/test_study_lib.py`](https://github.com/sefaav/quant-research-notebooks/blob/d44ae7a332b2a35a914a27897094723730b45cfb/pairs_trading_stationarity/test_study_lib.py)
  - Audit Artifacts & Numerical Tables: [`pairs_trading_stationarity/results/`](https://github.com/sefaav/quant-research-notebooks/tree/d44ae7a332b2a35a914a27897094723730b45cfb/pairs_trading_stationarity/results) (`metadata.json`, `inference.json`, `portfolio_metrics.csv`, `robustness.csv`, `selection.csv`, `persistence_tests.csv`, `performance_by_group.csv`, `dependence_robustness.csv`)
  - Platform Engine Dependency: Built on QuantLab (commit `62384eb475c93e90aeab8de1654d16d4aa0e0860`)
- **Verification Integrity:** All empirical figures, hypothesis test p-values, bootstrap intervals, and regression specifications were verified directly from raw code, executed notebook cells, and committed JSON/CSV audit tables. No search snippets, secondary blog summaries, or model-generated synthetic summaries were used to extract strategy mechanics or empirical findings.
- **Repository Deduplication Audit:** A full audit across existing records in `alpha-strategy-research` confirmed zero pre-existing captures citing `sefaav/quant-research-notebooks` or commit `d44ae7a332b2a35a914a27897094723730b45cfb`. Adjacent records in the repository evaluate related but structurally distinct cointegration systems:
  - `johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12.md` (Batra 2026, commit `fe031d51`) tests Johansen vector error-correction basket trading with Bayesian optimization and identifies execution friction asymmetry;
  - `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md` evaluates 4-way OU estimators across equity sector pairs;
  - `crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11.md` focuses on crypto perpetual funding-rate Kalman tracking.
  The current study provides an independent, pre-registered walk-forward falsification targeting the foundational assumption of quantitative pairs trading: whether in-sample Augmented Dickey-Fuller (ADF) stationarity filtering delivers out-of-sample alpha or merely selects for transient variance compression.

## Economic mechanism

### Source-reported

1. **Foundational Industry Paradigm:** In textbook and practitioner statistical arbitrage (e.g., Gatev, Goetzmann & Rouwenhorst 2006; Chan 2013), candidate asset pairs are screened over a historical formation window using the Augmented Dickey-Fuller (ADF) test on the residual spread $\hat\varepsilon_t = a_t - (\alpha + \beta b_t)$. A low p-value ($p < 0.05$) is conventionally treated as proof of mean-reversion, justifying an out-of-sample trading allocation under the expectation that the spread will continue to mean-revert (`source-reported`).
2. **Core Falsification Thesis:** The ADF test characterizes in-sample backward-looking residual dynamics, not forward-looking economic stability. Filtering candidate pairs by formation-window ADF rejection ($p < 0.05$) provides zero detectable out-of-sample performance benefit over unfiltered pairs when both groups are traded with identical rules, costs, and capital allocation (`source-reported`).
3. **The Variance-Compression Selection Bias:** The formation ADF filter systematically selects pairs that experienced an uncharacteristically calm, low-volatility formation window rather than structurally cointegrated relationships. In the out-of-sample trading window, these spreads suffer volatility expansion ($\sigma_{\text{OOS}} / \sigma_F$ median 1.20 for passing pairs vs 0.86 for failing pairs, $p < 0.0001$). This volatility expansion causes spread z-scores to blow through entry thresholds into the stop-loss zone ($|z| > 4.0$), generating severe stop losses and 50.6% higher turnover without compensatory return (`source-reported`).
4. **Decoupling of Stationarity Persistence:** In-sample stationarity does not persist into the subsequent trading window. The out-of-sample unit root rejection rate for formation-passing pairs (8.1%) is statistically indistinguishable from formation-failing pairs (7.2%, fold-clustered $p = 0.44$) (`source-reported`).

### Research interpretation

The Augmented Dickey-Fuller test is mathematically ill-suited as an alpha filter in pairs trading because unit-root test power is sensitive to sample variance and transitory regime quiescence. Over a 252-day formation window, an economically unlinked pair that happens to remain tightly bounded will exhibit a small residual variance, deflating the test denominator and producing an artificially low ADF p-value. When market conditions normalize or enter turbulence in the subsequent 126 days, variance expands toward its unconditional mean, shattering the frozen z-score bands. Consequently, in-sample ADF testing functions primarily as an opportunistic low-volatility screener that guarantees negative selection bias out of sample.

## Signal

### Formation timestamp & cadence
Signals are evaluated at the daily close of each trading day ($t$) using frozen formation parameters. Execution occurs at the open of the next trading session ($t+1$) via QuantLab's `next_bar_open` timing (`source-reported`).

### Lookback & walk-forward architecture
- **Formation Window ($F$):** 252 trading days (~12 months) of daily data (`source-reported`).
- **Trading Window ($T$):** 126 trading days (~6 months) of unseen out-of-sample data (`source-reported`).
- **Walk-Forward Folds:** 34 sequential folds spanning 2008-12-31 to 2026-01-12. Trading windows never overlap; formation windows overlap by 50% (126 days) (`source-reported`).
- **Frozen Formation Estimates:**
  - OLS regression of $a_t = \alpha + \beta b_t$ on formation rows, where assets $a$ and $b$ are oriented alphabetically ($a < b$) to prevent cherry-picking orientation (`source-reported`).
  - Formation spread: $\hat\varepsilon_t = a_t - (\alpha + \beta b_t)$ (`source-reported`).
  - Frozen spread mean: $\mu_F = \frac{1}{F}\sum_{t=1}^F \hat\varepsilon_t$ (`source-reported`).
  - Frozen spread standard deviation: $\sigma_F = \sqrt{\frac{1}{F-1}\sum_{t=1}^F (\hat\varepsilon_t - \mu_F)^2}$ (`source-reported`).
  - Formation ADF test: Standard `adfuller` test on $\hat\varepsilon_t$, yielding test statistic and p-value (`source-reported`).
- **Eligibility Filter:** Pair is classified as eligible if formation ADF p-value $< 0.05$ (`ADF_THRESHOLD = 0.05`) (`source-reported`).

### Normalized trading rule
During trading window days $t \in [F, F + T - 1]$, calculate the daily z-score using frozen parameters:
$$z_t = \frac{(a_t - (\alpha + \beta b_t)) - \mu_F}{\sigma_F}$$
The state machine updates position state $s_t \in \{-1.0, 0.0, 1.0\}$:
- **Long Entry ($s_t = +1.0$):** Triggered when $z_t < -2.0$ (`entry_z = 2.0`, long asset $a$, short asset $b$) (`source-reported`).
- **Short Entry ($s_t = -1.0$):** Triggered when $z_t > 2.0$ (`entry_z = 2.0`, short asset $a$, long asset $b$) (`source-reported`).
- **Mean-Reversion Exit ($s_t = 0.0$):**
  - If long ($s = +1.0$): exit to flat when $z_t > -0.5$ (`exit_z = 0.5`) (`source-reported`).
  - If short ($s = -1.0$): exit to flat when $z_t < 0.5$ (`exit_z = 0.5`) (`source-reported`).
- **Structural Break Stop-Loss ($s_t = 0.0$):** Forced exit to flat if $|z_t| > 4.0$ (`stop_z = 4.0`) (`source-reported`).
- **Boundary Precision:** Strict inequalities ($> / <$) are enforced; sitting exactly on boundary values does not trigger transitions (`source-reported`).
- **Window Closeout:** The last two days of the 126-day trading window are forced flat ($s_t = 0.0$) to guarantee all positions close and clear transaction costs within the active window (`source-reported`).

### Position sizing & capital allocation
- **Unit Gross Exposure:** Fixed leverage where $|w_a| + |w_b| = 1.0$ at trade entry (`source-reported`):
  $$w_{a, \text{entry}} = \frac{s \cdot P_{a, t}}{|s P_{a, t}| + |-s \beta P_{b, t}|}, \quad w_{b, \text{entry}} = \frac{-s \beta P_{b, t}}{|s P_{a, t}| + |-s \beta P_{b, t}|}$$
- **Weight Drift:** Between rebalances, QuantLab allows weights to drift naturally with asset prices; no synthetic intraday rebalancing occurs (`source-reported`).
- **Portfolio Policy:** Equal capital allocation across all eligible pairs in a fold ($1/N_{\text{eligible}}$ per pair sleeve), compounding independently without intra-window rebalancing (`source-reported`).

## Required data

- **Universe:** 25 liquid US ETFs structured into 3 non-overlapping economic clusters, yielding 92 within-cluster candidate pairs (`source-reported`):
  1. *US Sectors (9 symbols, 36 pairs):* XLB, XLE, XLF, XLI, XLK, XLP, XLU, XLV, XLY (`source-reported`).
  2. *Developed Market Equities (8 symbols, 28 pairs):* EWA, EWC, EWG, EWU, EWJ, EWQ, EWH, EWS (`source-reported`).
  3. *Fixed Income / Credit (8 symbols, 28 pairs):* TLT, IEF, LQD, HYG, JNK, AGG, EMB, TIP (`source-reported`).
- **Data Source:** Yahoo Finance daily bars via QuantLab DataLoader (`source-reported`).
- **Data Period:** 2008-01-02 to 2026-06-30 (4,652 trading days; 34 non-overlapping trading windows covering 2008-12-31 to 2026-01-12, with 116 trailing days unused) (`source-reported`).
- **Fields:** Adjusted close prices and overnight returns (close $t$ to open $t+1$) (`source-reported`).
- **Cache Verification:** Parquet dataset cache verified with SHA256 hash `4702a1aea9215375eb193fd941d6733ba23f96c3874c44bf8c23a9bbb2cf2ad7` (`source-reported`).
- **Point-in-Time Integrity:** Formation estimates are frozen at day $F-1$; no subsequent trading-window data leaks into $\alpha, \beta, \mu_F, \sigma_F$, or ADF statistics (`source-reported`).

## Execution assumptions

- **Signal-to-Order Timing:** `next_bar_open`. Decisions made at day $t$ close are executed at day $t+1$ market open (`source-reported`).
- **Overnight Decomposition:** QuantLab splits day $t+1$ returns into overnight return (close $t \to$ open $t+1$ accrued to the previous day's position) and intraday return (open $t+1 \to$ close $t+1$ accrued to the new position) (`source-reported`).
- **Execution Cost Model:**
  - Broker Commission: 2.0 basis points per leg (`commission_bps = 2.0`) (`source-reported`).
  - Half-Spread: 1.5 basis points per leg (`spread_bps = 3.0` quoted spread) (`source-reported`).
  - Slippage: 2.0 basis points per leg (`slippage_bps = 2.0`) (`source-reported`).
  - Total One-Way Turnover Cost: 5.5 basis points of capital turned over (`source-reported`).
  - Total Round-Trip Cost: 11.0 basis points per complete pair round-trip (`source-reported`).
- **Borrow & Shorting:** Frictionless shorting assumed for US ETFs; borrow fees omitted (`data gap`) (`source-reported`).
- **Market Impact:** Linear cost model; non-linear capacity impact omitted (`data gap`) (`source-reported`).

## Evidence

### Source-reported

All quantitative figures below are directly reported from `sefaav/quant-research-notebooks` (commit `d44ae7a332b2a35a914a27897094723730b45cfb`, September 11, 2026) across 3,128 pair-fold evaluations over 34 walk-forward folds (2008–2026):

1. **Selection Filter Behavior (`selection.csv`):**
   - Total pair-fold observations: 3,128.
   - Passing pairs ($p < 0.05$): 631 pair-folds (20.17% of candidate set).
   - Failing pairs ($p \ge 0.05$): 2,497 pair-folds (79.83% of candidate set).
   - Trade participation rate: 91.13% of passing pairs executed at least one trade vs 84.06% of failing pairs.
   - Mean trade entries per 126-day window: 2.84 entries for passing pairs vs 1.89 for failing pairs (+50.6% higher turnover).
   - Negative hedge ratio ($\hat\beta < 0$): 6.66% of passing pairs vs 8.81% of failing pairs.

2. **Out-of-Sample Performance by Group (`performance_by_group.csv`):**
   - Mean net return per window: Passing pairs $-0.613\%$ vs Failing pairs $-0.313\%$ (difference: $-0.300$ pp).
   - Median net return per window: Passing pairs $-0.285\%$ vs Failing pairs $0.000\%$.
   - 5th percentile return: Passing pairs $-6.151\%$ vs Failing pairs $-6.702\%$.
   - Share of positive windows: Passing pairs $37.24\%$ vs Failing pairs $36.60\%$.
   - Mean gross return (pre-cost): Passing pairs $-0.303\%$ vs Failing pairs $-0.108\%$.
   - Median Sharpe (traded pairs): Passing pairs $-0.394$ vs Failing pairs $-0.267$.
   - Median maximum drawdown: Passing pairs $-2.363\%$ vs Failing pairs $-2.495\%$.

3. **Statistical Panel Inference (`inference.json`, `dependence_robustness.csv`):**
   - **Fold-Clustered Fama-MacBeth Test:** Mean difference (eligible minus ineligible) = $-0.248$ pp per window, standard error = $0.204$ pp, $t = -1.216$, two-sided $p = 0.2325$, $95\%$ CI $[-0.662, +0.167]$ pp. Passing pairs outperformed failing pairs in only 16 of 34 folds ($47.06\%$).
   - **Newey-West HAC Test (2-fold lag):** Mean difference = $-0.248$ pp, $95\%$ CI $[-0.669, +0.173]$ pp, $p = 0.2396$.
   - **Circular Block Bootstrap (blocks of 3 folds, 5,000 draws):** Mean difference = $-0.248$ pp, $95\%$ CI $[-0.675, +0.144]$ pp, $p = 0.2272$.
   - **Two-Way Clustered Regression (fold + pair):** Coefficient = $-0.365$ pp, standard error = $0.221$ pp, $95\%$ CI $[-0.798, +0.067]$ pp, $p = 0.0977$.

4. **Portfolio-Level Comparison (`portfolio_metrics.csv`):**
   - **ADF-Filtered Portfolio ($p < 0.05$, avg 18.56 pairs held):** Annualized Sharpe = $-0.6076$, Annual Volatility = $1.78\%$, CAGR = $-1.09\%$, Max Drawdown = $-20.66\%$.
   - **Unfiltered Portfolio (all 92 candidate pairs held):** Annualized Sharpe = $-0.4661$, Annual Volatility = $1.61\%$, CAGR = $-0.76\%$, Max Drawdown = $-16.22\%$.
   - **Sharpe Difference ($\Delta\text{Sharpe}$):** $-0.1415$, $95\%$ paired cluster-bootstrap CI $[-0.5189, +0.2596]$, $p = 0.5031$. Filtered portfolio won in only 16 of 34 folds.

5. **Stationarity Persistence & Spread Variance Tests (`persistence_tests.csv`):**
   - **OOS ADF Rejection Rate:** Passing pairs $8.1\%$ vs Failing pairs $7.2\%$. Difference: $+1.31$ pp, $95\%$ CI $[-2.07, +4.68]$ pp, $p = 0.4368$ (null hypothesis of equal persistence cannot be rejected).
   - **Spread Standard Deviation Expansion ($\sigma_{\text{OOS}} / \sigma_F$):** Passing pairs median ratio $1.20$ vs Failing pairs median ratio $0.86$. Fold-clustered mean difference = $+0.4597$ ($+45.97$ pp), $95\%$ CI $[+0.3488, +0.5707]$, $t = 8.16$, $p = 9.61 \times 10^{-10}$. Passing pairs exhibit severe post-formation variance expansion.

6. **Robustness Variations across 7 Alternative Designs (`robustness.csv`):**
   - *Shorter Formation (126 days, 35 folds):* Mean diff $+0.236$ pp, $p = 0.443$, $\Delta\text{Sharpe} = +0.191$ ($[-0.328, +0.697]$); unfiltered portfolio Sharpe $-0.824$, filtered Sharpe $-0.633$.
   - *Longer Formation (504 days, 32 folds):* Mean diff $-0.376$ pp, $p = 0.226$, $\Delta\text{Sharpe} = -0.322$ ($[-0.816, +0.204]$); unfiltered Sharpe $-0.300$, filtered Sharpe $-0.622$.
   - *Gross of Costs (0x costs):* Mean diff $-0.135$ pp, $p = 0.507$, $\Delta\text{Sharpe} = -0.067$ ($[-0.407, +0.315]$); unfiltered Sharpe $-0.183$, filtered Sharpe $-0.250$.
   - *Double Costs (2x costs, 22 bps round-trip):* Mean diff $-0.360$ pp, $p = 0.092$, $\Delta\text{Sharpe} = -0.215$ ($[-0.612, +0.192]$); unfiltered Sharpe $-0.748$, filtered Sharpe $-0.963$.
   - *Reversed Orientation ($b$ on $a$):* Mean diff $-0.129$ pp, $p = 0.515$, $\Delta\text{Sharpe} = +0.029$ ($[-0.351, +0.410]$); unfiltered Sharpe $-0.600$, filtered Sharpe $-0.572$.
   - *Positive Hedge Ratio Only ($\hat\beta > 0$):* Mean diff $-0.150$ pp, $p = 0.426$, $\Delta\text{Sharpe} = -0.047$ ($[-0.423, +0.355]$); unfiltered Sharpe $-0.436$, filtered Sharpe $-0.484$.
   - *Engle-Granger Two-Step Cointegration Test Filter (8.92% pass rate):* Mean diff $-0.282$ pp, $p = 0.272$, $\Delta\text{Sharpe} = -0.067$ ($[-0.526, +0.460]$); unfiltered Sharpe $-0.466$, filtered Sharpe $-0.533$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The entirety of this empirical study represents rigorous negative evidence against a textbook quantitative heuristic:
- **No Performance Alpha:** Across all 34 walk-forward folds, the ADF filter consistently fails to generate positive excess returns ($p = 0.23$), degrading portfolio Sharpe ratio by $-0.14$.
- **No Stationarity Persistence:** Out-of-sample unit root rejection occurs in only $8.1\%$ of passing pairs, essentially indistinguishable from the $7.2\%$ rate observed in failing pairs ($p = 0.44$).
- **Selection Trap Proven:** The filter acts as an unintended variance filter, systematically picking pairs during transient volatility troughs ($p = 9.61 \times 10^{-10}$) which subsequently mean-revert into higher volatility out-of-sample.

## Falsification plan

To falsify the author's null/negative conclusion and demonstrate that an in-sample stationarity filter can deliver genuine out-of-sample value, an empirical experiment must satisfy the following pre-declared criteria:

1. **Universe & Asset Class Separation:** Evaluate candidate pools outside US ETFs, such as single-stock equities with verified supply-chain ties, commodity futures spreads (e.g., crack or crush spreads), or cross-venue crypto perpetual funding spreads (`research-proposed`).
2. **Dynamic / Time-Varying Estimation:** Replace static frozen OLS with dynamic state-space Kalman filtering or rolling cointegration vectors to test whether parameter drift rescues the filter (`research-proposed`).
3. **Volatility-Adjusted / Variance-Standardized Filtering:** Screen candidate pairs on ADF p-value conditioned on formation volatility being near or above its long-term unconditional median ($\sigma_F \ge \text{median}(\sigma_{2Y})$), directly eliminating the low-volatility selection artifact (`research-proposed`).
4. **Falsification Acceptance Thresholds:**
   - A candidate stationarity filter must achieve a statistically significant Fama-MacBeth return difference ($p < 0.01$, two-sided) net of 11 bps execution friction across at least 20 non-overlapping walk-forward folds (`research-defined falsification threshold`).
   - The out-of-sample stationarity persistence rate must exceed the failing group by at least 15 percentage points ($p < 0.01$) (`research-defined falsification threshold`).
   - The filtered portfolio Sharpe ratio must exceed the unfiltered candidate portfolio by at least $+0.30$ ($p < 0.05$ under block bootstrap) (`research-defined falsification threshold`).
5. **Action on Failure:** If conditioned or dynamic stationarity filters still fail to produce positive out-of-sample Sharpe differences, permanently retire formation ADF filtering from statistical arbitrage pipelines and rely solely on structural economic links and real-time spread tracking (`research-proposed`).

## Crypto portability

- **Portability Classification:** `adapted` / `unproven` (`research interpretation`).
- **Mechanism Portability Assessment:**
  - In crypto perpetual futures, pairs trading is commonly applied across correlated altcoin pairs against BTC/ETH or within thematic sectors (e.g., L1s, DeFi, AI tokens).
  - The risk of in-sample stationarity test failure is substantially **higher** in crypto than in US ETFs due to frequent regime shifts, token listing/delisting cycles, low liquidity, extreme volatility clustering, and exchange liquidation cascades.
  - Crypto perpetual pairs introduce continuous funding-rate carry costs. A pair whose price spread appears stationary over a 90-day formation window may carry severe funding rate divergence that bleeds capital faster than the spread mean-reverts.
  - Testing ADF stationarity filters on crypto perpetuals without funding-rate adjustments and dynamic liquidation guards is strongly unproven and likely subject to even more catastrophic variance expansion blowouts.

## Limitations

- **Baseline Trading Rule Unprofitability:** The underlying z-score rule had no edge across the evaluation period (losing money across both passing and failing groups, median traded Sharpe $-0.31$). The study proves that the ADF filter does not improve this specific rule, but cannot rule out that an ADF filter might interact beneficially with a rule possessing positive unconditional alpha (`source-reported`).
- **Static Linear Hedge Ratio:** Formation OLS estimates ($\alpha, \beta$) were frozen for 126 trading days. Real-world institutional stat-arb typically refits hedge ratios dynamically (e.g., daily rolling OLS or Kalman filters) (`source-reported`).
- **Fixed-Width Stop Loss:** The stop loss is set at $|z| > 4.0$ relative to frozen formation standard deviation $\sigma_F$. Because passing pairs experience variance expansion, their z-scores mechanically cross 4.0 even when the underlying price spread has not suffered an economic break (`source-reported`).
- **Survivorship in ETF List:** The 25 ETFs reflect a current survivor list; liquidated or merged funds from 2008–2026 are absent (`source-reported`).
- **Linear Friction Assumption:** Execution costs are modeled at fixed 11 bps round-trip without market impact or borrow fees (`source-reported`).

## Implementation status

`not-implemented`. This document captures external empirical research and methodological falsification for intake review. No implementation in `nautilus-quant-system`, PyBroker, or live execution engines has occurred.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`
- This record serves as a methodological warning and negative benchmark for statistical arbitrage pipelines. It does not authorize strategy implementation, paper trading, testnet, or live trading.

## Related Wiki records

- [[johansen-cointegration-etf-pairs-friction-asymmetry-falsification-2026-09-12]] — Batra 2026 60-pair ETF study demonstrating execution friction asymmetry and z-score stop failure under rolling volatility expansion.
- [[sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]] — S&P 500 statistical arbitrage evaluation with Johansen vector error correction and Hansen SPA testing.
- [[crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]] — Statistical arbitrage PCA-residual cointegration falsification in crypto markets.
- [[crypto-perpetual-pairs-trading-kalman-cointegration-falsification-2026-09-11]] — Walk-forward Kalman cointegration tracking and funding friction on crypto perpetuals.

## Sources

1. **sefaav.** *"Does ADF filtering actually improve pairs-trading performance out-of-sample? A walk-forward experiment on 92 economically related ETF pairs, 2008–2026."* Public GitHub repository `sefaav/quant-research-notebooks`, commit `d44ae7a332b2a35a914a27897094723730b45cfb`, published September 11, 2026.
   - Repository: [https://github.com/sefaav/quant-research-notebooks](https://github.com/sefaav/quant-research-notebooks)
   - Commit Tree: [https://github.com/sefaav/quant-research-notebooks/tree/d44ae7a332b2a35a914a27897094723730b45cfb](https://github.com/sefaav/quant-research-notebooks/tree/d44ae7a332b2a35a914a27897094723730b45cfb)
   - Primary Research Notebook: [`pairs_trading_stationarity/study.ipynb`](https://github.com/sefaav/quant-research-notebooks/blob/d44ae7a332b2a35a914a27897094723730b45cfb/pairs_trading_stationarity/study.ipynb)
   - Code Implementation: [`pairs_trading_stationarity/study_lib.py`](https://github.com/sefaav/quant-research-notebooks/blob/d44ae7a332b2a35a914a27897094723730b45cfb/pairs_trading_stationarity/study_lib.py)
   - Test Suite: [`pairs_trading_stationarity/test_study_lib.py`](https://github.com/sefaav/quant-research-notebooks/blob/d44ae7a332b2a35a914a27897094723730b45cfb/pairs_trading_stationarity/test_study_lib.py)
   - Audit Datasets & Metrics:
     - `pairs_trading_stationarity/results/metadata.json`
     - `pairs_trading_stationarity/results/inference.json`
     - `pairs_trading_stationarity/results/portfolio_metrics.csv`
     - `pairs_trading_stationarity/results/robustness.csv`
     - `pairs_trading_stationarity/results/selection.csv`
     - `pairs_trading_stationarity/results/persistence_tests.csv`
     - `pairs_trading_stationarity/results/performance_by_group.csv`
     - `pairs_trading_stationarity/results/dependence_robustness.csv`
2. **Underlying Methodology References Cited by Primary Source:**
   - Engle, R. F., & Granger, C. W. (1987). Co-integration and error correction: representation, estimation, and testing. *Econometrica*, 251-276.
   - Gatev, E., Goetzmann, W. N., & Rouwenhorst, K. G. (2006). Pairs trading: Performance of a relative-value arbitrage rule. *The Review of Financial Studies*, 19(3), 797-827.
   - Chan, E. P. (2013). *Algorithmic trading: winning strategies and their rationale*. John Wiley & Sons.
