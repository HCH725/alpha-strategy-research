---
schema: strategy-research-record-v1
title: "TETHER: Systematic Relative-Value Pairs Trading with Benjamini-Hochberg FDR Multiple-Testing Control, Ornstein-Uhlenbeck Half-Life Decay Scoring, Dynamic Net Book Beta Tracking, and Short-Borrow Frictions"
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
  - engle-granger
  - multiple-testing
  - fdr
  - benjamini-hochberg
  - kalman-filter
  - half-life
  - market-neutral
  - equities
  - negative-control
status: research-only
confidence: high
source_as_of: 2026-09-10
sources:
  - "Atharva Gite (atharva-gite), 'TETHER: Market-Neutral Relative Value Pairs Trading Desk', GitHub repository atharva-gite/pairstrading (commit f60b696d5ec48655382a1c6317463acd32668b05, September 10, 2026). Paths: README.md, src/logic.py, app.py, docs/ko-pep-vs-aapl-msft.md, tests/test_logic.py. Stable URL: https://github.com/atharva-gite/pairstrading"
  - "Atharva Gite, 'KO/PEP vs AAPL/MSFT: when correlation is not a book', TETHER RelVal desk walk-forward research note (September 2026). Stable path: docs/ko-pep-vs-aapl-msft.md, docs/ko-pep-vs-aapl-msft.pdf"
  - "Streamlit Web Application: https://atharva-gite-pairstrading.streamlit.app/ (as-of September 2026)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# TETHER: Systematic Relative-Value Pairs Trading with Benjamini-Hochberg FDR Multiple-Testing Control, Ornstein-Uhlenbeck Half-Life Decay Scoring, Dynamic Net Book Beta Tracking, and Short-Borrow Frictions

## Provenance

- **Author / Research Lab:** Atharva Gite (`atharva-gite`), *TETHER Market-Neutral Relative Value Pairs Desk*.
- **Primary Source Codebase:** Public GitHub repository `https://github.com/atharva-gite/pairstrading`.
- **Immutable Commit SHA:** `f60b696d5ec48655382a1c6317463acd32668b05` (main branch HEAD, September 10, 2026 14:23:07 UTC).
- **Inspected Primary Source Files:**
  - `README.md`: Architecture overview, walk-forward philosophy, FDR multiple testing rationale, negative control findings, execution and cost specifications.
  - `src/logic.py`: Core quant engine — Engle-Granger two-step cointegration test, Benjamini-Hochberg FDR and Bonferroni p-value corrections, discrete Ornstein-Uhlenbeck AR(1) half-life estimation, composite Tether Score formulation, 2D state-space Kalman filter hedge ratio tracker, rolling OLS hedge ratio estimator, benchmark beta regression, dynamic net book beta calculation, 1-bar lagged signal state machine, turnover transaction cost and daily short borrow fee accounting.
  - `app.py`: Interactive Streamlit trading terminal, sector universes (Energy, Consumer Staples, Technology, Financials, Healthcare), benchmark tickers (SPY, QQQ, DIA, IWM, XLK), state descriptions (`TETHERED`, `WEAK`, `BROKEN`).
  - `docs/ko-pep-vs-aapl-msft.md`: Walk-forward research note documenting empirical results for working hypothesis pair (KO/PEP) versus negative control pair (AAPL/MSFT).
  - `tests/test_logic.py`: Verification suite covering cointegration outputs, Kalman filter array shapes, signal generation, positive half-life constraints, gross dollar notional allocation under Hedge Ratio and Equal Dollar sizing, and multiple-testing ranking.
- **Repository Deduplication Audit:** A comprehensive audit of all records in `alpha-strategy-research` confirmed zero pre-existing captures citing Atharva Gite or repository `atharva-gite/pairstrading`. Related statistical arbitrage captures in the repository address different mechanisms and scopes:
  - `sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md` (Nguyen 2026, `Duyanh090205/pairs-trading-engine`) investigated unbounded beta drift and phantom P&L in Kalman filters when equity prices diverge.
  - `sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12.md` (Nock 2026) evaluated S&P 500 equity sector pairs using causal residualization and PCA hedge ratio asymmetry.
  - `sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12.md` (pdwi2020 2026) evaluated multi-asset Johansen cointegration with OU ablation.
  - `crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12.md` (Barredo Lago 2026) investigated 50-token perpetual futures intraday PCA factor residuals.
  - `crypto-pairs-trading-walk-forward-cointegration-hurst-2026-09-12.md` (etoh0305 2026) evaluated Binance perpetual futures pairs using Hurst exponents.
  Atharva Gite's research contributes an independent, self-contained market-neutral relative value framework featuring Benjamini-Hochberg FDR correction across sector universes, a composite half-life and stability metric ("Tether Score"), dynamic net market beta exposure tracking ($\beta_{\text{net}}$ vs SPY), and an explicit empirical negative control (AAPL/MSFT) demonstrating that high return correlation fails to generate a tradable mean-reverting spread.

## Economic mechanism

### Source-reported

The author posits that classical pairs trading fails in production because practitioners confuse co-movement (return correlation) with a stationary, mean-reverting economic tether (cointegration). 

In equities, companies sharing common fundamental cost structures, regulatory environments, and consumer demand (e.g., consumer staples such as Coca-Cola and PepsiCo, or energy producers such as ExxonMobil and Chevron) are tied together by long-run economic substitution. Temporary dislocations driven by institutional rebalancing, liquidity shocks, or transient earnings divergence push the log-price spread away from equilibrium, creating a mean-reverting statistical arbitrage opportunity.

Conversely, high correlation driven by shared exposure to a broad macroeconomic or tech factor (e.g., Apple and Microsoft) does not establish an economic tether. When two tech giants experience structural divergence or unequal earnings growth, the spread drifts without mean-reverting force. Testing pairs with raw p-values across a universe guarantees false discoveries due to multiple hypothesis testing. Furthermore, supposedly market-neutral books often leak substantial directional market beta because dynamic hedge ratios ($ \beta $) alter leg notionals over time, exposing the trader to unhedged market drift. Finally, borrowing stock to short is not frictionless; unmodeled short borrow fees erode thin statistical arbitrage margins.

### Research interpretation

The hypothesized mechanism is **sector-level relative-value mean reversion under strict multiple-testing and risk-neutrality constraints**. 

The strategy combines five interdependent operational components:
1. **Multiple-Testing Family-Wise Control:** Sector-constrained pairwise cointegration screening under Benjamini-Hochberg False Discovery Rate (FDR) control ($q < 0.05$) to eliminate spurious statistical associations among $C(N, 2)$ combinations.
2. **Structural Quality Scoring (Tether Score):** Multi-factor structural appraisal combining Engle-Granger p-value significance, ADF residual stationarity, Ornstein-Uhlenbeck half-life speed (penalizing execution churn when $t_{\text{half}} < 5$ days and macro drift when $t_{\text{half}} > 60$ days), and hedge ratio stability ($CV_\beta$).
3. **Walk-Forward Temporal Isolation:** Complete out-of-sample partitioning where cointegration parameters, hedge ratios ($\beta_{\text{frozen}}$), and equilibrium intercepts ($\alpha_{\text{frozen}}$) are estimated exclusively on a historical discovery window (pre-2024-01-01) and frozen during out-of-sample execution (post-2024-01-01), tracking explicit post-split death (`tether_died`).
4. **Dynamic Net Market Beta Monitoring:** Continuous measurement of the dollar-weighted market exposure against SPY:
   $$\beta_{\text{net}, t} = \frac{\text{held}_{A, t} \cdot \beta_A^{\text{SPY}} + \text{held}_{B, t} \cdot \beta_B^{\text{SPY}}}{\text{capital}}$$
   ensuring that dynamic Kalman filter or rolling OLS adjustments do not inadvertently convert a pairs trade into a hidden directional index bet.
5. **Frictional Realism:** Full accounting of two-sided turnover transaction costs (10 bps slippage + 5 bps commission = 15 bps per unit turnover) and continuous annualized short-borrow financing fees (50 bps default accrued daily on short dollar notional).

## Signal

### Formation timestamp
- **Data frequency:** Daily closing prices (`Close`) downloaded via `yfinance` (`src/logic.py`, line 69).
- **Signal formation:** Formed at the close of trading day $t$ using trailing prices up to and including day $t$.
- **Execution convention:** 1-bar execution delay (`pos_lag = positions.shift(1).fillna(0.0)`, `src/logic.py`, line 681). Positions established on day $t$ earn return on day $t+1$, completely eliminating same-bar look-ahead bias.

### Lookback windows
- **Walk-forward discovery split:** Pre-split data ($\le$ `2024-01-01`) used for initial cointegration screening, FDR evaluation, and hedge calibration. Minimum 60 discovery observations and 40 out-of-sample observations required (`src/logic.py`, line 655).
- **Z-score estimation window:** Rolling $W = 30$ trading days (`src/logic.py`, line 640).
- **Rolling cointegration evaluation window:** Rolling $W_{\text{coint}} = 126$ trading days (approx. 6 calendar months), evaluated at a 10-day step cadence (`src/logic.py`, line 348).
- **Rolling OLS window (optional mode):** Rolling $W_{\text{ols}} = 30$ trading days (`src/logic.py`, line 173).

### Mathematical formulation

1. **Log Price Transformation:**
   $$y_t = \ln(P_{A, t}), \quad x_t = \ln(P_{B, t})$$

2. **Cointegration and Hedge Calibration:**
   Static OLS estimation on the discovery sample:
   $$y_t = \beta x_t + \alpha + \epsilon_t$$
   Engle-Granger cointegration test computes test statistic and asymptotic p-value $p_{\text{coint}}$.
   Augmented Dickey-Fuller test on the residual spread $\epsilon_t$ computes $p_{\text{adf}}$.

3. **Multiple-Testing FDR Correction:**
   For a sector of $N$ assets, all $M = C(N, 2) = \frac{N(N-1)}{2}$ pairwise tests are evaluated.
   Raw p-values $p_{(1)} \le p_{(2)} \le \dots \le p_{(M)}$ are adjusted using the Benjamini-Hochberg procedure:
   $$p_{\text{fdr}, (i)} = \min_{j \ge i} \left\{ \min\left(1, \frac{M}{j} p_{(j)}\right) \right\}$$
   A pair is deemed FDR-significant if $p_{\text{fdr}} \le \alpha_{\text{fdr}}$ (default $\alpha_{\text{fdr}} = 0.05$). Bonferroni significance is also reported: $p_{\text{bonf}} = \min(1, M \cdot p)$.

4. **Ornstein-Uhlenbeck Half-Life:**
   Discrete AR(1) specification on the spread:
   $$\Delta \epsilon_t = \lambda \epsilon_{t-1} + \mu + \eta_t$$
   Estimated via OLS. If $\lambda \ge 0$, the process does not mean-revert ($t_{\text{half}} = \text{NaN}$).
   If $\lambda < 0$:
   $$t_{\text{half}} = -\frac{\ln 2}{\lambda} \text{ trading days}$$

5. **Tether Score Formulation (`compute_tether_profile`):**
   A normalized score $S_{\text{tether}} \in [0, 100]$ evaluates pair viability:
   $$S_{\text{tether}} = 100 \times \left(0.40 \cdot s_p + 0.20 \cdot s_{\text{adf}} + 0.25 \cdot s_{\text{hl}} + 0.15 \cdot s_{\text{stab}}\right)$$
   where:
   - $s_p = \text{clip}\left(1.0 - \frac{p_{\text{coint}}}{0.10}, 0.0, 1.0\right)$
   - $s_{\text{adf}} = \text{clip}\left(1.0 - \frac{p_{\text{adf}}}{0.10}, 0.0, 1.0\right)$
   - Half-life score $s_{\text{hl}}$:
     $$s_{\text{hl}} = \begin{cases} 
     1.00 & \text{if } 8.0 \le t_{\text{half}} \le 40.0 \\ 
     0.75 & \text{if } 5.0 \le t_{\text{half}} \le 60.0 \text{ (and not in } [8, 40]\text{)} \\ 
     0.35 & \text{if } t_{\text{half}} < 5.0 \\ 
     \text{clip}\left(1.0 - \frac{t_{\text{half}} - 60.0}{120.0}, 0.0, 0.40\right) & \text{if } t_{\text{half}} > 60.0 \\ 
     0.00 & \text{if } t_{\text{half}} \le 0 \text{ or non-finite} 
     \end{cases}$$
   - Stability score $s_{\text{stab}}$:
     If dynamic beta series $\beta_t$ is available (length $\ge 8$):
     $$CV_\beta = \frac{\sigma(\beta)}{|\mu(\beta)| + 10^{-8}}, \quad s_{\text{stab}} = \text{clip}\left(\frac{1.0}{1.0 + CV_\beta}, 0.0, 1.0\right)$$
     Otherwise, default $s_{\text{stab}} = 0.80$.
   - **Tether State Classification:**
     - `TETHERED`: $S_{\text{tether}} \ge 70$ and $p_{\text{coint}} < 0.05$.
     - `WEAK`: $S_{\text{tether}} \ge 45$ and $p_{\text{coint}} < 0.10$.
     - `BROKEN`: all other pairs.

6. **State-Space Kalman Filter Hedge (Optional Mode):**
   State vector $\theta_t = [\beta_t, \alpha_t]^T$:
   - Observation equation: $y_t = [x_t, 1] \theta_t + v_t, \quad v_t \sim \mathcal{N}(0, V), \quad V = 10^{-3}$
   - Transition equation: $\theta_t = \theta_{t-1} + w_t, \quad w_t \sim \mathcal{N}(0, W), \quad W = \frac{\delta}{1 - \delta} I_2, \quad \delta = 10^{-5}$
   Provides causal, online tracking of beta and alpha without future look-ahead.

7. **Rolling Z-Score Calculation:**
   Spread definition:
   $$\text{spread}_t = y_t - (\beta_t x_t + \alpha_t)$$
   Rolling statistics over lookback $W = 30$:
   $$\mu_{\text{spread}, t} = \frac{1}{W} \sum_{i=0}^{W-1} \text{spread}_{t-i}, \quad \sigma_{\text{spread}, t} = \sqrt{\frac{1}{W-1} \sum_{i=0}^{W-1} (\text{spread}_{t-i} - \mu_{\text{spread}, t})^2}$$
   $$z_t = \frac{\text{spread}_t - \mu_{\text{spread}, t}}{\sigma_{\text{spread}, t}}$$

8. **Position State Machine (`build_signals`):**
   Signal state $S_t \in \{-1, 0, 1\}$:
   - When flat ($S_{t-1} = 0$):
     - If $z_t < -\text{entry\_z}$ ($-2.0$): enter Long spread ($S_t = +1$, long asset A, short asset B).
     - If $z_t > +\text{entry\_z}$ ($+2.0$): enter Short spread ($S_t = -1$, short asset A, long asset B).
     - Otherwise: maintain flat ($S_t = 0$).
   - When Long spread ($S_{t-1} = +1$):
     - If $z_t \ge -\text{exit\_z}$ ($-0.5$): exit to flat ($S_t = 0$, mean-reversion profit take).
     - If $z_t \le -\text{stop\_loss}$ ($-3.0$): exit to flat ($S_t = 0$, structural break stop-loss).
     - If $z_t > +\text{entry\_z}$ ($+2.0$): flip to Short spread ($S_t = -1$).
     - Otherwise: hold Long ($S_t = +1$).
   - When Short spread ($S_{t-1} = -1$):
     - If $z_t \le +\text{exit\_z}$ ($+0.5$): exit to flat ($S_t = 0$, mean-reversion profit take).
     - If $z_t \ge +\text{stop\_loss}$ ($+3.0$): exit to flat ($S_t = 0$, structural break stop-loss).
     - If $z_t < -\text{entry\_z}$ ($-2.0$): flip to Long spread ($S_t = +1$).
     - Otherwise: hold Short ($S_t = -1$).

9. **Capital Allocation & Dollar Notionals:**
   Using 1-bar lagged beta $\beta_{t-1}$ to prevent look-ahead:
   - **Hedge Ratio Sizing:**
     $$|A_t| + |B_t| = C \quad \text{with } |B_t| = |\beta_{t-1}| |A_t|$$
     $$N_{A, t} = \frac{C}{1.0 + |\beta_{t-1}|}, \quad N_{B, t} = N_{A, t} \cdot \beta_{t-1}$$
   - **Equal Dollar Sizing:**
     $$N_{A, t} = \frac{C}{2.0}, \quad N_{B, t} = \text{sign}(\beta_{t-1}) \cdot \frac{C}{2.0}$$
   Dollar holdings:
   $$\text{held}_{A, t} = S_{t-1} \cdot N_{A, t}, \quad \text{held}_{B, t} = -S_{t-1} \cdot N_{B, t}$$

10. **P&L, Friction, and Financing Accounting:**
    - Gross daily return:
      $$\text{pnl}_{\text{gross}, t} = \text{held}_{A, t} \cdot r_{A, t} + \text{held}_{B, t} \cdot r_{B, t}$$
      where $r_{A, t} = \ln(P_{A, t}) - \ln(P_{A, t-1})$.
    - Turnover transaction costs:
      $$\text{Turnover}_t = |\text{held}_{A, t} - \text{held}_{A, t-1}| + |\text{held}_{B, t} - \text{held}_{B, t-1}|$$
      $$\text{Cost}_{\text{trans}, t} = \text{Turnover}_t \times (c_{\text{comm}} + c_{\text{slip}}) = \text{Turnover}_t \times (0.0005 + 0.0010) = \text{Turnover}_t \times 15\text{ bps}$$
    - Daily short borrow cost:
      $$\text{ShortNotional}_t = |\min(0, \text{held}_{A, t})| + |\min(0, \text{held}_{B, t})|$$
      $$\text{Cost}_{\text{borrow}, t} = \text{ShortNotional}_t \times \frac{c_{\text{borrow}}}{252} = \text{ShortNotional}_t \times \frac{0.0050}{252}$$
    - Net daily dollar P&L:
      $$\text{pnl}_{\text{net}, t} = \text{pnl}_{\text{gross}, t} - \text{Cost}_{\text{trans}, t} - \text{Cost}_{\text{borrow}, t}$$
      $$r_{\text{strat}, t} = \frac{\text{pnl}_{\text{net}, t}}{C}$$

## Required data

- **Universe:** Sector constituents across 5 equity sectors (`SECTOR_UNIVERSES`, `src/logic.py` lines 23-29):
  - *Energy:* XOM, CVX, COP, BP, SHEL ($M = 10$ pairs).
  - *Consumer Staples:* KO, PEP, PG, WMT, COST ($M = 10$ pairs).
  - *Technology:* AAPL, MSFT, GOOGL, META, NVDA, AMD ($M = 15$ pairs).
  - *Financials:* JPM, BAC, WFC, GS, MS ($M = 10$ pairs).
  - *Healthcare:* JNJ, PFE, UNH, ABBV, MRK ($M = 10$ pairs).
- **Benchmarks:** SPY (default), QQQ, DIA, IWM, XLK.
- **Fields:** Daily closing prices (`Close`) adjusted for splits and dividends via `yfinance`.
- **Venue:** US Equities (NYSE / NASDAQ).
- **Timeframe:** 1-day bar sampling, standard US equity trading calendar.
- **Point-in-time conventions:** Split date `2024-01-01` strictly delineates in-sample discovery from out-of-sample execution. In-sample estimation uses only prices before the split timestamp.

## Execution assumptions

- **Order timing:** Daily close-to-close with an explicit 1-bar execution delay (`pos_lag = positions.shift(1)`). Signals evaluated at close $t$ are entered at close $t+1$.
- **Order type:** Modeled as closing market orders with explicit friction penalties.
- **Transaction costs (source-reported):**
  - Commission: $5\text{ bps}$ ($0.0005$ of traded notional).
  - Slippage: $10\text{ bps}$ ($0.0010$ of traded notional).
  - Combined round-turn execution friction: $15\text{ bps}$ per unit turnover.
- **Financing and borrow costs (source-reported):**
  - Short borrow fee: $50\text{ bps}$ annualized ($0.0050$), charged daily across 252 trading days on the absolute dollar notional of the short leg.
- **Capital base (source-reported):** $C = \$100,000$ initial capital.
- **Leverage / margin:** $1.0\times$ gross capital leverage ($|A| + |B| = C$). No naked leverage or uncovered margin expansion.
- **Fill model:** 100% fill rate assumed on liquid mega-cap equities at modeled prices minus slippage and commission.

## Evidence

### Source-reported

The author documents empirical backtest and diagnostic results across several key tests in `docs/ko-pep-vs-aapl-msft.md`, `README.md`, and the Streamlit application:

1. **Negative Control Verification (AAPL / MSFT):**
   - **Tether State:** Explicitly classified as `BROKEN`.
   - **Tether Score:** $\sim 25$ out of $100$.
   - **Ornstein-Uhlenbeck Half-Life:** $\sim 114$ trading days (vastly exceeding the target $8\text{--}40$ day window).
   - **Rolling Cointegration:** Rolling 126-day Engle-Granger p-values persistently drift above the $0.05$ threshold, proving that the spread decays into two unhedged directional bets.
   - **On-Time Exit Diagnostic:** Exits evaluated against $1.5 \times t_{\text{half}} \approx 171$ days are identified as statistically meaningless; almost any round-trip will close over a half-year horizon, producing an illusion of trade timeliness.
2. **Working Hypothesis (KO / PEP):**
   - Classified as a valid consumer-staples economic tether with shared distribution, identical input cost exposure, and low market beta divergence.
   - Evaluated under strict walk-forward split (discovery $\le$ `2024-01-01`, trading post-`2024-01-01`) with frozen OLS hedge ratio $\beta_{\text{frozen}}$.
   - Author explicitly mandates that if out-of-sample Sharpe ratio degrades relative to in-sample discovery, that negative result remains displayed on the desk rather than retuning parameters.
3. **Multiple Testing Attrition:**
   - Demonstrates that a 5-stock sector generating 10 pairwise combinations produces multiple false-positive cointegration signals at a nominal raw $p < 0.05$.
   - Application of Benjamini-Hochberg FDR control at $\alpha = 0.05$ eliminates spurious candidates, reducing candidate pairs to a robust subset.
4. **Net Market Beta Leakage:**
   - Documents that when dynamic Kalman filtering or rolling OLS is selected, drift in $\beta_t$ causes leg notionals to drift, introducing significant net market beta ($\beta_{\text{net}} \ne 0$) against SPY.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly designed the project to highlight negative evidence and failure modes:
1. **Correlation is Not Cointegration:** High correlation pairs (AAPL/MSFT) completely fail cointegration and half-life filters, generating unhedged directional losses.
2. **Walk-Forward Attrition (`tether_died`):** Pairs identified as cointegrated (`TETHERED`) during historical discovery frequently experience structural breaks out-of-sample, transitioning to `BROKEN` post-2024.
3. **Friction Sensitivity:** Zero-cost backtests produce deceptively smooth equity curves. Incorporating 15 bps turnover friction and 50 bps annualized borrow fee substantially reduces net Sharpe and can push borderline pairs into net negative P&L.
4. **Beta Leakage in Dynamic Hedging:** Dynamic Kalman hedges intended to adapt to regime shifts often inflate directional index beta risk, undermining true market neutrality.

## Falsification plan

To falsify the TETHER alpha thesis and its risk-scoring mechanism:

1. **Multiple-Testing Survival Hurdle (`research-defined falsification threshold`):**
   - Evaluate all $C(N, 2)$ pairs across S&P 500 GICS sectors.
   - If fewer than $5\%$ of raw cointegrated pairs ($p < 0.05$) survive Benjamini-Hochberg FDR correction at $q = 0.05$, the raw cointegration phenomenon in equities is dominated by selection noise.
2. **Walk-Forward Performance Retention (`research-defined falsification threshold`):**
   - Using a 3-year discovery window and 1-year forward holdout, measure out-of-sample Sharpe ratio ($SR_{\text{OOS}}$) versus in-sample Sharpe ratio ($SR_{\text{IS}}$).
   - If $SR_{\text{OOS}} \le 0.0$ or $SR_{\text{OOS}} < 0.35 \times SR_{\text{IS}}$ across more than $60\%$ of `TETHERED` pairs, reject the thesis that the Tether Score reliably predicts tradable out-of-sample persistence.
3. **Half-Life Speed Boundary Test (`research-defined falsification threshold`):**
   - Partition pairs into three bins: Fast ($t_{\text{half}} < 5$ days), Medium ($8 \le t_{\text{half}} \le 40$ days), and Slow ($t_{\text{half}} > 60$ days).
   - After applying 15 bps turnover friction, the Fast bin must exhibit net negative Sharpe due to turnover drag.
   - The Slow bin must exhibit net beta drift and drawdown exceeding $20\%$.
   - If the Medium bin does not outperform both the Fast and Slow bins on net risk-adjusted return ($p < 0.05$), the non-linear half-life scoring heuristic is falsified.
4. **Net Market Beta Neutrality Stress (`research-defined falsification threshold`):**
   - Regress daily strategy returns against SPY returns during market stress regimes (SPY 20-day realized volatility $> 25\%$ or 5-day drawdown $> 5\%$).
   - If strategy exposure $|t(\beta_{\text{market}})| > 2.0$ (statistically significant directional exposure), the pair construction is falsified as a market-neutral relative-value strategy.
5. **Short-Borrow Cost Ladder (`research-defined falsification threshold`):**
   - Stress short borrow costs from 50 bps to 300 bps annualized.
   - If median strategy net return turns negative at borrow costs $\le 100\text{ bps}$, the edge is economically unviable outside institutional prime brokerage rebate tiers.

## Crypto portability

**Portability Classification:** `adapted` / `unproven`.

The TETHER framework was formulated and evaluated on US cash equities. Porting the mechanism to cryptocurrency perpetual futures requires substantial structural modifications (`research-proposed`):

1. **Perpetual-to-Perpetual Funding Rate Drift:**
   In cash equities, holding a short leg incurs explicit stock borrow fees ($50\text{ bps}$ annualized). In cryptocurrency perpetual swaps, shorting does not incur a stock borrow fee; instead, both legs are subject to 8-hour funding rates. If asset A and asset B have divergent average funding rates (e.g., altcoin funding rate $+30\text{ bps}$ per day vs BTC $+3\text{ bps}$ per day), the cumulative spread will experience continuous deterministic drift, destroying log-price cointegration. A crypto adaptation must model the **funding-adjusted log price spread**:
   $$\tilde{y}_t = \ln P_{A, t} - \sum_{s=1}^t F_{A, s}, \quad \tilde{x}_t = \ln P_{B, t} - \sum_{s=1}^t F_{B, s}$$
2. **24/7 Continuous Trading & Timestamp Alignment:**
   Unlike equities with unified 09:30-16:00 EST trading sessions and official daily closing auctions, crypto markets trade continuously. Daily bar boundaries must be standardized (e.g., 00:00:00 UTC) across exchanges to avoid artificial asynchronous price distortions.
3. **Execution Frictions & Fee Asymmetry:**
   Taker fees on major crypto exchanges (2.0 to 5.0 bps) and bid-ask spreads on altcoins are wider than large-cap US equities. Turnover-driven mean-reversion with a 30-day lookback may generate excessive friction unless executed via passive post-only limit orders.
4. **Liquidation Cascades & Fat-Tailed Divergence:**
   In equities, hard stop-losses at $|z| \ge 3.0$ mitigate divergence. In crypto perpetuals, leveraged liquidation cascades can blow through statistical boundaries, creating extreme non-linear excursions that fail standard Gaussian z-score assumptions. Dynamic volatility targeting or wider stop-loss bands (`research-proposed`) are required.

## Limitations

- **Small Sector Universe:** The default sectors contain only 5 to 6 tickers each ($10\text{ to }15$ pairs per sector). While suitable for multiple-testing demonstrations, institutional statistical arbitrage typically screens hundreds of cross-sectional assets.
- **Simplified OLS and Cointegration:** Standard Engle-Granger two-step cointegration assumes a fixed alphabetical orientation ($\ln P_A$ on $\ln P_B$) rather than Johansen maximum eigenvalue or orthogonal distance regression, making the hedge ratio dependent on variable ordering.
- **Point-in-Time Universe Survivorship:** The sector tickers represent current large-cap survivors, introducing survivorship bias into historical 2019-2023 discovery backtests.
- **Unverified Crypto Efficacy:** The primary source does not demonstrate the strategy on cryptocurrency pairs; any application to digital assets remains an adapted research hypothesis.
- **Fixed Z-Score Thresholds:** Symmetric entry ($\pm 2.0$) and exit ($\pm 0.5$) thresholds are heuristically chosen rather than analytically optimized via first-passage time stochastic control.

## Implementation status

`not-implemented`.

This research capture records external research methodology and source code from `atharva-gite/pairstrading`. No implementation has been created in `nautilus-quant-system`, PyBroker, or NautilusTrader.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`

This record is a normalized research artifact staged for ChatGPT Research Intake Review. Presence in this repository does not constitute validation, backtest endorsement, paper trading approval, testnet verification, or live trading authorization.

## Related Wiki records

- `[[quant/sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12]]`
- `[[quant/sp500-sector-pairs-causal-residual-pca-area-asymmetry-2026-09-12]]`
- `[[quant/sp500-statistical-arbitrage-johansen-ou-ablation-multiple-testing-2026-09-12]]`
- `[[quant/crypto-pairs-trading-walk-forward-cointegration-hurst-2026-09-12]]`
- `[[quant/crypto-perpetual-pca-factor-residual-reversion-falsification-2026-09-12]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`

## Sources

1. **Primary Codebase & Documentation:**
   Atharva Gite (`atharva-gite`), *TETHER: Market-Neutral Relative Value Pairs Trading Desk*, GitHub repository `https://github.com/atharva-gite/pairstrading`, commit SHA `f60b696d5ec48655382a1c6317463acd32668b05` (September 10, 2026).
   - Inspected files: `README.md`, `src/logic.py`, `app.py`, `docs/ko-pep-vs-aapl-msft.md`, `tests/test_logic.py`, `requirements.txt`.
2. **Research Note:**
   Atharva Gite, *"KO/PEP vs AAPL/MSFT: when correlation is not a book"*, TETHER RelVal desk walk-forward research note, September 2026. File: `docs/ko-pep-vs-aapl-msft.md`, `docs/ko-pep-vs-aapl-msft.pdf`.
3. **Interactive Research Application:**
   Atharva Gite, *TETHER Pairs Trading Streamlit App*, `https://atharva-gite-pairstrading.streamlit.app/` (accessed September 2026).
