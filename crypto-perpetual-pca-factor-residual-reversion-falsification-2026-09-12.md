---
schema: strategy-research-record-v1
title: "Crypto Perpetual Statistical Arbitrage: Empirical Falsification of Intraday PCA Factor-Residual Mean Reversion Under Realistic Turnover and Execution Costs"
created: 2026-09-12
updated: 2026-09-12
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - statistical-arbitrage
  - pca
  - mean-reversion
  - ornstein-uhlenbeck
  - turnover-control
  - negative-evidence
  - okx
status: research-only
confidence: high
source_as_of: 2026-08-28
sources:
  - "Carlos Barredo Lago (Qinvia Research), 'Factor-Residual Reversion in Crypto Perpetuals: A Cost-Aware Falsification Study', August 28, 2026. Editorial publication: https://qinvia.com/research/factor-residual-reversion"
  - "GitHub repository carlosbarredo/qinvia-crypto-factor-residual-reversion (commit fac56ac1deef4c660ff65867597b6944ee53d3fb, September 2026), paths: README.md, DATA.md, CITATION.cff, configs/study.json, artifacts/study-summary.json, src/factor_residual_experiment.py, src/factor_residual_continuation.py, notebooks/factor_residual_reversion_en.ipynb, scripts/build_figures.py"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Crypto Perpetual Statistical Arbitrage: Empirical Falsification of Intraday PCA Factor-Residual Mean Reversion Under Realistic Turnover and Execution Costs

## Provenance

- **Author / Research Lab:** Carlos Barredo Lago (`carlosbarredo`), Qinvia Research.
- **Editorial Publication:** *"Factor-Residual Reversion in Crypto Perpetuals: A Cost-Aware Falsification Study"*, Qinvia Research (August 28, 2026), [https://qinvia.com/research/factor-residual-reversion](https://qinvia.com/research/factor-residual-reversion).
- **Primary Source Codebase:** Public GitHub repository `https://github.com/carlosbarredo/qinvia-crypto-factor-residual-reversion`.
- **Immutable Commit SHA:** `fac56ac1deef4c660ff65867597b6944ee53d3fb` (main branch HEAD, September 7, 2026; release tagged 2026-08-28).
- **Inspected Primary Source Artifacts:**
  - `README.md`, `README_ES.md`: Headline empirical findings, research narrative, replication steps, citation metadata.
  - `DATA.md`: Data specification, 50-asset OKX USDT perpetual contract universe, 15-minute bar construction from 1-minute historical candles, quality controls, omission of funding.
  - `CITATION.cff`: Citation schema (v1.2.0), author attribution, date released (2026-08-28).
  - `configs/study.json`: Authoritative parameter registry for the 81-configuration baseline, continuation frozen recipe, turnover cost ladder, and pre-registered governance hurdle.
  - `artifacts/study-summary.json`: Structured machine-readable empirical results for baseline and final grid, decision rule verdict.
  - `src/factor_residual_experiment.py`: Core baseline pipeline — 15-minute rolling PCA factor extraction, Marchenko-Pastur bulk threshold diagnostics, residual return calculation, rolling Ornstein-Uhlenbeck AR(1) s-score calculation, Dickey-Fuller stationarity filter, raw alpha state machine, exact nullspace factor/dollar-neutral projection, and daily return compounding.
  - `src/factor_residual_continuation.py`: Continuation pipeline — Stage 1 turnover reduction levers (box-constrained asset caps via Dykstra/OSQP, hysteresis entry/exit matrix, deadband rebalancing, execution cadence / action intervals, L1 ADMM turnover penalties, R2 variance quantile filtering, 2026 blind evaluation protocol, robustness envelopes).
  - `notebooks/factor_residual_reversion_en.ipynb`: Executable bilingual summary notebook verifying data contracts, configuration counts, and decision rule outcomes.
  - `scripts/build_figures.py`: Exact plotting routines and aggregation logic for cost sensitivity, capital curves, robustness maps, and temporal stability.
  - `tests/test_portfolio_constraints.py`: Unit test suite verifying dollar neutrality, factor neutrality, Dykstra projection bounds, causal curve calculations, and deadband flattening.
- **Source Evaluation Window:** April 1, 2024 00:00 UTC through August 27, 2026 23:45 UTC (over 2.4 years / 84,000+ 15-minute bars, following a 90-day initial warmup from January 1, 2024).
- **Repository Deduplication Audit:** A comprehensive audit of all existing strategy records in `alpha-strategy-research` confirmed zero pre-existing records citing Carlos Barredo Lago, Qinvia Research, or repository `carlosbarredo/qinvia-crypto-factor-residual-reversion`. Related statistical arbitrage records in the repository examine different universes, time horizons, or market structures:
  - `crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12.md` (Bryan Vine 2026, Paper 3) investigated daily/hourly Binance spot data and Engle-Granger pairs trading.
  - `sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12.md` (Nock 2026) evaluated S&P 500 equity sector pairs.
  - `eurostoxx-pca-ou-stat-arb-trading-time-friction-falsification-2026-09-12.md` (Cerrone et al. 2026) evaluated Euro Stoxx 50 equities under clock vs volume trading-time sampling.
  - `funding-adjusted-cross-exchange-perp-price-space-arb-ou-s-score-illiquidity-guards-2026-09-12.md` (Ho & Chan 2026) examined cross-exchange perpetual spatial arbitrage across 4 major coins on 6 exchanges after stripping funding drift.
  - `crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md` (Kumar 2026) investigated 5-minute single-instrument crowded-flush reversals on Binance perpetuals.
  Barredo Lago's research constitutes an independent, 50-asset intraday (15-minute) perpetual futures statistical arbitrage study with pre-registered turnover-control levers, Dykstra/OSQP portfolio projection, and a pre-registered cost hurdle.

## Economic mechanism

### Source-reported

The author investigates whether equity-style statistical arbitrage—specifically the Avellaneda & Lee (2010) framework decomposing asset returns into systemic PCA factors and mean-reverting idiosyncratic residuals—can generate exploitable alpha in cryptocurrency perpetual swaps at high intraday frequencies (15-minute bars).

The theoretical thesis posits that broad cryptocurrency market movements are dominated by common systemic drivers (e.g., market-wide beta, Bitcoin and Ethereum directional trends, liquidity cycles), which are captured by the leading principal components of the return correlation matrix. Subtracting these common factor exposures yields idiosyncratic residual return series. When individual tokens experience transient order-flow imbalances, localized liquidation cascades, or retail overshooting, their cumulative residuals deviate from equilibrium. Assuming these dislocations are temporary, an Ornstein-Uhlenbeck (OU) mean-reverting process models the residual path, generating standardized s-score signals that trigger contrarian trades when residuals reach statistical extremes.

The core motivation of the study, however, is a deliberate cost-aware falsification test: while classical backtests in academic literature often report high gross Sharpe ratios by ignoring transaction costs or assuming frictionless execution, high-frequency intraday statistical arbitrage induces substantial turnover. The study systematically evaluates whether the gross residual mean-reversion alpha is robust enough to survive realistic taker fees, bid-ask spreads, and execution churn in cryptocurrency derivatives markets.

### Research interpretation

The hypothesized mechanism is **intraday idiosyncratic mean reversion in cryptocurrency perpetuals**. Systematic factor extraction removes systemic market risk, isolating token-specific noise. If market participants push idiosyncratic prices away from fundamental co-movement due to transient inventory imbalances or forced liquidations, mean reversion should follow as liquidity returns.

However, the critical economic friction demonstrated by this research is **the turnover-to-friction barrier**:
1. At a 15-minute bar frequency, mean-reversion cycles operate on horizons of 6 to 72 hours.
2. Capturing these brief deviations requires continuous portfolio rebalancing across dozens of assets, generating massive annual turnover (150x to over 500x).
3. In cryptocurrency perpetual markets, market participants incur two-sided taker fees (typically 2.0 to 5.0 bps on OKX depending on VIP tier), bid-ask spreads (1.0 to 3.0 bps on liquid perps, much wider on altcoins), and execution slippage.
4. Because the gross return generated per trade is only a few basis points, the transaction cost per unit of turnover rapidly overwhelms the gross statistical edge. The median strategy crosses below zero between 0.0 and 2.0 bps of cost per unit turnover.

**Component roles:**
- **Systemic factor filter:** Rolling 15-minute PCA correlation matrix decomposition ($K \in \{2, 3, 5\}$ factors over $W \in \{20, 30, 60\}$ days) to project out common market variance.
- **Idiosyncratic signal:** Rolling AR(1) Ornstein-Uhlenbeck process on cumulative residuals ($W_{\text{res}} \in \{7, 14, 30\}$ days) with Dickey-Fuller stationarity filter ($\tau \le -2.86$) and half-life bounds ($6 \le t_{\text{half}} \le 72$ hours) producing standardized s-scores.
- **Entry trigger:** S-score boundary breach ($|s| \ge \text{entry\_score}$), initiating contrarian long ($s < 0$) or short ($s > 0$) positions.
- **Exit trigger:** Reversion to equilibrium ($|s| \le \text{exit\_score}$), zero-crossing, stop-loss ($|s| \ge 4.0$), or timeout ($3 \times t_{\text{half}}$).
- **Turnover mitigation levers:** Deadband thresholding ($\delta = 0.20$), rebalance execution thinning (every 8 bars / 2 hours), and position hysteresis.
- **Portfolio projection:** Exact nullspace projection ensuring dollar neutrality ($\sum w_i = 0$) and factor neutrality ($w^T \Lambda = 0$) with normalized gross leverage ($\sum |w_i| = 1.0$).

## Signal

### Formation timestamp
- **Data frequency:** 15-minute bars constructed from 1-minute OHLCV candles, using the first 1-minute open price of each 15-minute interval (`DATA.md`).
- **Signal formation:** Evaluated at the start of each 15-minute bar using trailing historical prices up to the current bar open.
- **Tradable convention:** Same-open zero-lag screening convention where weights formed at bar $t$ earn return from $t$ to $t+1$ (`open[t]` to `open[t+1]`). The author explicitly documents this as an idealized research screen designed to test the alpha hypothesis rather than a live execution forecast (`README.md`, line 68).

### Lookback
- **Factor estimation window ($W_{\text{factor}}$):** 20, 30, or 60 days ($1,920$, $2,880$, or $5,760$ 15-minute bars). Recalibrated daily at 00:00 UTC (`src/factor_residual_experiment.py`, line 174).
- **Residual OU estimation window ($W_{\text{residual}}$):** 7, 14, or 30 days ($672$, $1,344$, or $2,880$ 15-minute bars). Continuously rolled on cumulative residuals (`src/factor_residual_experiment.py`, line 265).
- **Warmup period:** 90 days (January 1, 2024 00:00 UTC to April 1, 2024 00:00 UTC).

### Mathematical formulation

1. **Standardized Log Returns:**
   $$r_{t,i} = \ln\left(\frac{P_{t,i}^{\text{open}}}{P_{t-1,i}^{\text{open}}}\right), \quad \tilde{r}_{t,i} = \frac{r_{t,i} - \mu_i}{\sigma_i}$$
   where $\mu_i$ and $\sigma_i$ are the sample mean and sample standard deviation of asset $i$ over the trailing window $W_{\text{factor}}$.

2. **PCA Factor Extraction & Marchenko-Pastur Diagnostic:**
   $$C = \frac{1}{M-1} \tilde{R}^T \tilde{R} \in \mathbb{R}^{N \times N}$$
   Eigen-decomposition yields eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_N$ and eigenvectors $v_1, \dots, v_N$.
   The Marchenko-Pastur upper bulk limit is:
   $$\lambda_+ = \left(1 + \sqrt{\frac{N}{M}}\right)^2$$
   Factors $k \in \{1, \dots, K\}$ corresponding to the largest eigenvalues form the factor loading matrix:
   $$\Lambda_{i,k} = \sigma_i v_{i,k}$$
   The standardized residual return is:
   $$\epsilon_{t,i} = \sigma_i \left(\tilde{r}_{t,i} - \sum_{k=1}^K v_{i,k} \sum_{j=1}^N v_{j,k} \tilde{r}_{t,j}\right)$$

3. **Cumulative Residuals & Ornstein-Uhlenbeck Process:**
   Cumulative residuals are accumulated:
   $$X_{t,i} = \sum_{s=1}^t \epsilon_{s,i}$$
   Over a trailing window $W_{\text{residual}}$, $X_{t,i}$ is modeled as an AR(1) discrete Ornstein-Uhlenbeck process:
   $$X_{t,i} = a_i + b_i X_{t-1,i} + \eta_{t,i}, \quad \eta_{t,i} \sim \mathcal{N}(0, \sigma_{\eta,i}^2)$$
   - OLS regression estimates slope $b_i$ and intercept $a_i$.
   - Slope validity constraint: $0 < b_i < 1.0$.
   - Dickey-Fuller t-statistic: $\tau_i = \frac{b_i - 1}{\text{SE}(b_i)}$. Stationarity requires $\tau_i < -2.86$ (`DF_CRITICAL`, 5% critical value).
   - Half-life of mean reversion:
     $$t_{\text{half},i} = -\frac{\ln 2}{\ln b_i} \text{ bars}$$
     Filter requirement: $24.0 \le t_{\text{half},i} \le 288.0$ bars (6.0 hours to 72.0 hours).
   - Equilibrium mean and variance:
     $$m_i = \frac{a_i}{1 - b_i}, \quad \sigma_{\text{eq},i}^2 = \frac{\sigma_{\eta,i}^2}{1 - b_i^2}$$
   - Standardized s-score:
     $$s_{t,i} = \frac{X_{t,i} - m_i}{\sigma_{\text{eq},i}}$$

4. **Raw Alpha State Machine (`build_raw_alpha`):**
   For asset $i$ at bar $t$, position state $S_{t,i} \in \{-1, 0, 1\}$:
   - When flat ($S = 0$):
     - If $|s_{t,i}| \in [\text{entry\_score}, \text{stop\_score})$:
       - If $s_{t,i} < 0$: enter Long ($S_{t,i} = +1$, contrarian buy).
       - If $s_{t,i} > 0$: enter Short ($S_{t,i} = -1$, contrarian sell).
       - Maximum holding duration set to: $\text{age}_{\max} = \max(1, \text{round}(3.0 \times t_{\text{half},i}))$.
       - Raw alpha: $\alpha_{t,i} = S_{t,i} \times |s_{t,i}|$.
   - When active ($S \in \{-1, +1\}$):
     - Age incremented: $\text{age} \leftarrow \text{age} + 1$.
     - Exit triggered ($S \leftarrow 0, \alpha_{t,i} \leftarrow 0$) if any of:
       1. Score or half-life becomes invalid (NaN or Inf).
       2. Zero crossing: $(S = +1 \land s_{t,i} \ge 0) \lor (S = -1 \land s_{t,i} \le 0)$.
       3. Reversion target reached: $|s_{t,i}| \le \text{exit\_score}$.
       4. Stop-loss breached: $|s_{t,i}| \ge \text{stop\_score}$ ($4.0$).
       5. Holding timeout: $\text{age} \ge \text{age}_{\max}$.
     - Otherwise: maintain position, $\alpha_{t,i} = S_{t,i} \times |s_{t,i}|$.

5. **Portfolio Projection & Factor Neutralization (`project_and_normalize`):**
   Constraints matrix:
   $$C = [\mathbf{1}_N, \Lambda_K] \in \mathbb{R}^{N \times (K+1)}$$
   Projection onto nullspace of $C$:
   $$\tilde{w}_t = \alpha_t - \alpha_t C (C^T C)^{-1} C^T$$
   This ensures:
   - Dollar neutrality: $\sum_{i=1}^N \tilde{w}_{t,i} = 0$.
   - Factor neutrality: $\tilde{w}_t^T \Lambda_K = \mathbf{0}$.
   - Normalized gross leverage:
     $$w_{t,i} = \frac{\tilde{w}_{t,i}}{\sum_{j=1}^N |\tilde{w}_{t,j}|} \quad (\text{Gross exposure } = 1.0)$$

6. **Continuation Optimization Levers (`src/factor_residual_continuation.py`):**
   To mitigate turnover, the author tested six systematic levers:
   - **Lever A (Asset weight cap):** Box constraints $|w_i| \le c$ solved via Dykstra's projection or OSQP quadratic programming ($c \in \{0.10, 0.20, 0.35, \text{None}\}$). Result: Unlimited cap retained highest net Sharpe.
   - **Lever B1 (Hysteresis):** Wider entry/exit thresholds ($\text{entry} \in \{2.0, 2.5, 3.0\} \times \text{exit} \in \{0.0, 0.5, 1.0\}$). Result: Entry = 3.0, Exit = 0.0 (holding until exact mean crossing) produced greatest turnover reduction.
   - **Lever B2 (Deadband rebalancing):** Target weights are only adjusted if $|w_{t,i}^{\text{target}} - w_{t-1,i}| > \delta$ ($\delta \in \{0.0, 0.05, 0.10, 0.20\}$). Forced flattening to 0 on exit is always preserved. Result: $\delta = 0.20$ was optimal.
   - **Lever B3 (Execution cadence):** Rebalance only every $H \in \{1, 2, 4, 8\}$ bars (up to 2 hours). Result: $H = 8$ bars (every 2 hours) reduced turnover substantially.
   - **Lever B4 (L1 ADMM turnover penalty):** Objective $\min_w \frac{1}{2}\|w - w_{\text{target}}\|^2 + \lambda \|w - w_{t-1}\|_1$ ($\lambda \in \{0.0, 0.5, 1.0, 2.0\}$). Result: $\lambda = 0.0$ selected (did not provide incremental advantage over B1+B2+B3).
   - **Lever C ($R^2$ universe filtering):** Filter assets by trailing PCA explanatory power quantile ($q \in \{0.60, 0.80, 1.00\}$). Result: Failed pre-registered contribution gate (did not improve Sharpe by $\ge 0.25$ without increasing turnover).

### Parameters Summary

| Parameter | Baseline Values | Continuation Frozen Recipe | Classification |
|---|---|---|---|
| Bar resolution | 15 minutes | 15 minutes | Source-reported (`configs/study.json`) |
| Factor window ($W_{\text{factor}}$) | 20, 30, 60 days | 20, 30, 60 days | Source-reported (`configs/study.json`) |
| Number of factors ($K$) | 2, 3, 5 | 2, 3, 5 | Source-reported (`configs/study.json`) |
| Residual window ($W_{\text{residual}}$) | 7, 14, 30 days | 7, 14, 30 days | Source-reported (`configs/study.json`) |
| Entry score | 1.5, 2.0, 2.5 | 3.0 | Source-reported (`configs/study.json`) |
| Exit score | 0.5 | 0.0 (zero crossing) | Source-reported (`configs/study.json`) |
| Stop score | 4.0 | 4.0 | Source-reported (`configs/study.json`) |
| Half-life bounds | [24.0, 288.0] bars (6–72h) | [24.0, 288.0] bars (6–72h) | Source-reported (`src/factor_residual_experiment.py`) |
| Dickey-Fuller critical $\tau$ | -2.86 (5% level) | -2.86 | Source-reported (`src/factor_residual_experiment.py`) |
| Deadband ($\delta$) | 0.0 | 0.20 | Source-reported (`configs/study.json`) |
| Rebalance cadence | 1 bar (15m) | 8 bars (2 hours) | Source-reported (`configs/study.json`) |
| Asset weight cap | None | None (unlimited) | Source-reported (`configs/study.json`) |
| Turnover penalty $\lambda$ | 0.0 | 0.0 | Source-reported (`configs/study.json`) |
| $R^2$ universe quantile | 1.00 (all assets) | 1.00 (all assets) | Source-reported (`configs/study.json`) |
| Governance cost hurdle | 3.5 bps | 3.5 bps | Source-reported (`configs/study.json`) |

## Required data

- **Instrument / Universe:** 50 USDT-margined perpetual swap contracts on OKX:
  `ETH, BTC, SOL, XRP, DOGE, BICO, PEPE, WLD, SUI, LINK, ONT, BNB, UNI, AAVE, ADA, LTC, BCH, NEAR, FIL, STX, AVAX, SHIB, XLM, CRV, DOT, PEOPLE, TRX, ORDI, INJ, OP, APT, ETC, ICP, GAS, ARB, PYTH, LDO, HBAR, ATOM, ALGO, CORE, GALA, MINA, TIA, ENS, TRB, CFX, AXS, SAND, MAGIC` (`DATA.md`).
- **Venue:** OKX perpetual swaps market.
- **Timeframe:** 15-minute bars aggregated from 1-minute historical candles.
- **Price field:** First 1-minute `open` price of each 15-minute interval.
- **Timestamping:** UTC epoch milliseconds.
- **Missing-data & Quality Filters:**
  - `MIN_VALID_ASSETS`: At least 20 valid assets required in the trailing window to fit the factor model.
  - `MAX_ZERO_FRACTION`: Assets with $> 20\%$ zero-return bars in the trailing window are excluded.
  - `MAX_ZERO_RUN_BARS`: Assets with $> 32$ consecutive zero-return bars (8 hours) are excluded.
  - Non-finite returns or prices $\le 0$ rejected.
  - Log returns calculated only across finite, strictly positive prices.
- **Funding, Spread, and Fee Data:**
  - **Funding rates:** Intentionally omitted from this price-only study (`DATA.md`, line 72: *"Funding is intentionally omitted from this price-only experiment. Funding/basis carry is a separate research branch"*).
  - **Fees & slippage:** Modeled parametrically as a fixed transaction cost per unit of turnover across a ladder: $c \in \{0.0, 2.0, 3.5, 5.0, 7.0, 10.0\}$ bps.

## Execution assumptions

- **Signal-to-order timing:** Zero-lag research screening convention where portfolio weights formed at the open of bar $t$ earn return from $\text{open}_t$ to $\text{open}_{t+1}$. The author notes that this overstates live trading PnL because orders cannot be executed simultaneously with the observation bar open without latency.
- **Fill model:** Instantaneous fill at the 15-minute bar open price.
- **Turnover calculation:**
  $$T_t = \sum_{i=1}^N |w_{t,i} - w_{t-1,i}|$$
- **Net return calculation:**
  $$r_t^{\text{net}} = r_t^{\text{gross}} - c \cdot T_t$$
  where $c$ is the transaction cost per unit turnover.
- **Leverage & Margin:**
  - Net exposure: Exactly $0.0$ (dollar-neutral).
  - Factor exposure: Exactly $\mathbf{0}$ (neutral to top $K$ PCA factors).
  - Gross exposure: Exactly $1.0$ (100% total gross notional, 50% long / 50% short).
- **Borrow & Shorting:** Symmetric long and short execution assumed natively in perpetual swaps without locate fees or borrow constraints.

## Evidence

### Source-reported

All figures below are directly reported by Carlos Barredo Lago in `artifacts/study-summary.json`, `README.md`, `configs/study.json`, and `notebooks/factor_residual_reversion_en.ipynb` over the evaluation period from April 1, 2024 through August 27, 2026:

#### Baseline Experiment (81 Configurations)
- **Total configurations evaluated:** 81 ($3 \times 3 \times 3 \times 3$ grid of $W_{\text{factor}} \in \{20, 30, 60\} \times K \in \{2, 3, 5\} \times W_{\text{residual}} \in \{7, 14, 30\} \times \text{entry} \in \{1.5, 2.0, 2.5\}$).
- **Gross-positive fraction:** **91.4%** (74 of 81 configurations achieve positive gross Sharpe before costs).
- **Median Sharpe at 3.5 bps governance cost:** **−3.44**.
- **Positive configurations at 3.5 bps governance cost:** **1.2%** (only 1 of 81 configurations survived costs).
- **Cost breakeven:** The median strategy crossed below zero before 1.0 bps of cost per unit turnover.

#### Final Locked Grid (27 Configurations)
Following the bounded continuation experiments incorporating Lever B1 (entry=3.0, exit=0.0), Lever B2 (deadband=0.20), Lever B3 (action every 8 bars / 2 hours), and Lever A (unlimited cap):
- **Total configurations in final grid:** 27 ($3 \times 3 \times 3$ grid of $W_{\text{factor}}, K, W_{\text{residual}}$).
- **Median gross Sharpe:** **+0.358**.
- **Gross-positive fraction:** **74.1%** (20 of 27 configurations).
- **Median annual turnover:** **150.1×** (reduced substantially from the baseline rate of $>500\times$, but still elevated).
- **Median Sharpe at 3.5 bps governance cost:** **−0.213**.
- **Positive configurations at 3.5 bps governance cost:** **33.3%** (9 of 27 configurations).
- **Cost breakeven:** The median final configuration crosses below zero between 0.0 and 2.0 bps per unit turnover.
- **Pre-registered decision rule verdict:**
  - *Rule:* *"Close the branch if the median final-grid Sharpe at 3.5 bps is not positive."* (`configs/study.json`, line 31).
  - *Result:* Median Sharpe is −0.213 ($\le 0$).
  - *Action:* **FAIL CLOSED**. The author formally closed the 15-minute PCA-residual research branch (`artifacts/study-summary.json`, line 17: *"Close the 15-minute PCA-residual branch and move to a separately specified hypothesis"*).

### Independently reproduced

`not independently reproduced`. Scout research capture; full source code, configuration files, test suites, and empirical artifacts inspected and verified directly from GitHub repository `carlosbarredo/qinvia-crypto-factor-residual-reversion` commit `fac56ac1deef4c660ff65867597b6944ee53d3fb`.

### Negative evidence

1. **Catastrophic friction fragility:** While 91.4% of baseline configurations produce positive gross returns, 98.8% collapse into severe net losses at 3.5 bps of friction. The median baseline Sharpe drops from positive to −3.44.
2. **Turnover wall:** Despite aggressive optimization (deadband filtering, 2-hour execution cadence thinning, and wide entry/exit hysteresis), annual turnover could not be reduced below 150.1x without destroying the gross alpha signal.
3. **Failure of L1 turnover regularization:** The L1 ADMM turnover penalty ($\lambda \in \{0.5, 1.0, 2.0\}$) failed to improve net Sharpe relative to heuristic deadband and cadence controls, indicating that mathematical shrinkage of weight movement distorts factor neutrality or dampens the highest-conviction trades.
4. **Failure of $R^2$ variance filtering:** Restricting the universe to tokens with high factor explanatory power ($R^2$ quantiles 0.60 and 0.80) failed the pre-registered contribution gate (did not improve Sharpe by $\ge 0.25$), showing that residual reversion is not concentrated in "cleaner" factor models.
5. **Omission of funding drag:** In live perpetual trading, holding unhedged long/short portfolios across 50 tokens introduces substantial funding rate carry risk. Because funding rates were omitted, true live performance would likely suffer additional divergence or liquidation risk.

## Falsification plan

### Primary Source Pre-Registered Falsification (Executed)
- **Hurdle:** Median daily Sharpe ratio of the 27-configuration final grid at 3.5 bps cost per unit turnover must exceed 0.0 over the full sample (`configs/study.json`).
- **Observed Result:** Median Sharpe = −0.213; only 33.3% positive (`source-reported`).
- **Verdict:** **FALSIFIED**. The 15-minute PCA-residual mean-reversion hypothesis is rejected as unviable under realistic market frictions (`source-reported`).

### Additional Research-Proposed Falsification Tests

1. **Execution Lag Stress Test (`research-proposed`):**
   - *Protocol:* Replace the same-open zero-lag convention ($w_t$ earning return from $\text{open}_t$ to $\text{open}_{t+1}$) with a causal 1-bar execution delay ($w_t$ executed at $\text{open}_{t+1}$, earning return from $\text{open}_{t+1}$ to $\text{open}_{t+2}$).
   - *Decision rule (`research-defined falsification threshold`):* If median gross Sharpe drops below 0.0 under 1-bar execution delay, the gross residual reversion effect is falsified as an artifact of same-bar timing alignment.

2. **Order-Book Depth & Slippage Stress Test (`research-proposed`):**
   - *Protocol:* Replace the linear turnover fee model with empirical volume-weighted average price (VWAP) fills from OKX Level-2 order book depth snapshots for order sizes of $10,000, $50,000, and $250,000.
   - *Decision rule (`research-defined falsification threshold`):* If effective two-way execution costs exceed 4.0 bps at a $50,000 portfolio size, the strategy is falsified as unexecutable at institutional scale.

3. **Funding Rate Carry Integration (`research-proposed`):**
   - *Protocol:* Incorporate realized 8-hour OKX funding settlement payments for all 50 perpetual contracts into the backtest ledger.
   - *Decision rule (`research-defined falsification threshold`):* If funding payments reduce annualized net returns by $> 250$ bps or increase maximum drawdown by $> 5.0\%$, the hypothesis that residual reversion can be harvested independently of funding carry is falsified.

4. **Timeframe Horizon Ablation (1h vs 4h vs 15m) (`research-proposed`):**
   - *Protocol:* Re-estimate the PCA-residual framework on 1-hour and 4-hour bars using identical rolling factor and residual parameters scaled to bar counts.
   - *Decision rule (`research-defined falsification threshold`):* If annual turnover falls below 35x while gross Sharpe remains $> 0.40$ and net Sharpe at 3.5 bps exceeds 0.20, the hypothesis of residual mean reversion survives at lower frequencies; otherwise, factor-residual statistical arbitrage is rejected across all intraday crypto horizons.

## Crypto portability

**direct**

The strategy was natively designed, implemented, and tested on cryptocurrency perpetual futures (50 OKX USDT-margined contracts). No adaptation from traditional equities or commodities is required.

Crypto-specific structural considerations:
- **Perpetual swap mechanics:** Allows seamless two-sided shorting without equity locate fees or borrow recall risk, which is a major advantage over traditional stock pairs trading.
- **24/7 continuous session:** Eliminates overnight gaps and market open/close auction anomalies found in equity statistical arbitrage.
- **Funding rate drag:** Perpetuals settle funding every 8 hours. Holding idiosyncratic long/short baskets creates unintended directional funding exposure unless explicitly constrained by a funding-neutral projection (`research-proposed`).
- **Exchange contract specifications:** OKX perpetual contracts have contract multipliers (`ctVal`), tick sizes, and minimum lot sizes (`lotSz`) that create rounding indivisibilities for smaller portfolio sizes (`source-reported` in `DATA.md`).
- **Liquidity disparity:** Large tokens (BTC, ETH, SOL) exhibit tight spreads (<1 bps), whereas smaller altcoins in the 50-token universe (MAGIC, GAS, TRB) experience frequent liquidity vacuums and wide spreads (>10 bps) during volatility events.

## Limitations

- **Negative result:** The strategy failed its pre-registered cost hurdle and is not profitable after realistic fees.
- **Same-open execution bias:** Weights at bar $t$ earn return from $\text{open}_t$ to $\text{open}_{t+1}$, introducing an unmodeled zero-latency advantage in the backtest.
- **Funding rates omitted:** The study intentionally excluded funding payments, leaving unmeasured funding drag or carry asymmetry.
- **Survivorship bias in universe selection:** The 50-asset universe was frozen retrospectively from liquid OKX contracts as of 2024/2026, omitting tokens that were delisted during the sample period.
- **No paper or live trading:** All findings are derived from historical backtests; no forward paper, testnet, or production execution has occurred (`not independently reproduced`).

## Implementation status

`not-implemented`

No implementation of this strategy, the Dykstra/OSQP factor-neutral projection, or the deadband state machine exists in our PyBroker, NautilusTrader, Paper, Testnet, or Live execution repositories.

## Adoption boundary

This record is **research material only**. Presence in this repository does not imply:
- profitable strategy
- validated alpha
- approved for implementation
- approved for paper trading
- approved for testnet
- approved for live trading

The primary source author formally rejected and closed this research branch due to cost failure.

## Related Wiki records

- `[[quant/crypto-statistical-arbitrage-pca-residual-cointegration-falsification-2026-09-12]]` — Empirical falsification of daily/hourly spot PCA-residual OU mean reversion and Engle-Granger pairs on Binance (Vine 2026). Related: both examine PCA-residual statistical arbitrage in crypto; distinct: Vine evaluated spot daily/hourly data and liquidity tercile stale-price decay, while Barredo Lago evaluates 15-minute perpetual swaps with exact nullspace factor/dollar-neutral projection and turnover optimization.
- `[[quant/eurostoxx-pca-ou-stat-arb-trading-time-friction-falsification-2026-09-12]]` — Euro Stoxx 50 PCA stat-arb under trading-time and friction falsification (Cerrone et al. 2026). Related: both apply Avellaneda & Lee PCA-residual OU framework; distinct: Cerrone evaluated European equities under volume clock sampling.
- `[[quant/sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12.md]]` — S&P 500 sector stat-arb with causal residualization and PCA hedge ratios (Nock 2026). Related: PCA-residualization for mean reversion; distinct: equity sector pairs vs crypto perpetual cross-section.
- `[[quant/funding-adjusted-cross-exchange-perp-price-space-arb-ou-s-score-illiquidity-guards-2026-09-12.md]]` — Cross-exchange perpetual spatial arbitrage after funding adjustment (Ho & Chan 2026). Related: uses OU s-scores on perpetual futures; distinct: spatial cross-venue price-space arbitrage vs single-venue cross-sectional PCA residual arbitrage.
- `[[quant/crypto-perp-crowded-flush-reversal-microstructure-2026-09-12.md]]` — High-frequency crowded-flush reversal in crypto perpetuals (Kumar 2026). Related: high-frequency crypto perpetuals facing microstructure cost barriers; distinct: single-asset open-interest flush reversal vs 50-asset PCA factor residualization.

## Sources

1. Carlos Barredo Lago. "Factor-Residual Reversion in Crypto Perpetuals: A Cost-Aware Falsification Study." *Qinvia Research*, August 28, 2026. Editorial URL: [https://qinvia.com/research/factor-residual-reversion](https://qinvia.com/research/factor-residual-reversion).
2. Carlos Barredo Lago. `carlosbarredo/qinvia-crypto-factor-residual-reversion`. Public GitHub repository, commit `fac56ac1deef4c660ff65867597b6944ee53d3fb` (September 7, 2026). Key paths: `README.md`, `DATA.md`, `CITATION.cff`, `configs/study.json`, `artifacts/study-summary.json`, `src/factor_residual_experiment.py`, `src/factor_residual_continuation.py`, `notebooks/factor_residual_reversion_en.ipynb`, `scripts/build_figures.py`.
3. Marco Avellaneda and John Lee. "Statistical arbitrage in the US equities market." *Quantitative Finance* 10(7):761–782, 2010. DOI: [10.1080/14697680903124632](https://doi.org/10.1080/14697680903124632). (Foundational PCA factor extraction and OU s-score framework).
