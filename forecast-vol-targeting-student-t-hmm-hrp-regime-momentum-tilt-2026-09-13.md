---
schema: strategy-research-record-v1
title: Forecast-Volatility Targeted Student-t HMM Regime-Gated Hierarchical Risk Parity with Asymmetric Momentum Exposure Gating (KRONOS-TRADE / Oliverz 2026)
created: 2026-09-13
updated: 2026-09-13
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - equities
  - regime-switching
  - student-t-hmm
  - har-rv
  - risk-parity
  - hrp
  - black-litterman
  - volatility-targeting
  - falsification
status: research-only
confidence: medium
source_as_of: 2026-09-12
sources:
  - "Oliverz (Olivesz), 'KRONOS: Regime-aware quantitative alpha platform & market-microstructure research lab', public GitHub repository 'Olivesz/kronos-quant', commit 2e112e4e5f01a39d89121921df86ef2970e237a4 (September 2026). Stable repository URL: https://github.com/Olivesz/kronos-quant; Commit URL: https://github.com/Olivesz/kronos-quant/tree/2e112e4e5f01a39d89121921df86ef2970e237a4"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forecast-Volatility Targeted Student-t HMM Regime-Gated Hierarchical Risk Parity with Asymmetric Momentum Exposure Gating (KRONOS-TRADE / Oliverz 2026)

## Provenance

- **Author / Research Lab:** Oliverz (`Olivesz` on GitHub), KRONOS Quantitative Research Project.
- **Repository:** `https://github.com/Olivesz/kronos-quant` (`source-reported`).
- **Full Immutable Commit SHA:** `2e112e4e5f01a39d89121921df86ef2970e237a4` (`source-reported`).
- **Core Code & Research Paths:**
  - Trading System Implementation: [`kronos/trade.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/trade.py) (`source-reported`).
  - Master Configuration & Parameter Bounds: [`config.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/config.py) (`source-reported`).
  - Student-t Hidden Markov Model ECM Engine: [`kronos/thmm.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/thmm.py) (`source-reported`).
  - Volatility Laboratory & HAR-RV Estimator: [`kronos/vollab.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/vollab.py) (`source-reported`).
  - Cross-Sectional Factor Signals: [`kronos/signals.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/signals.py) (`source-reported`).
  - Risk Engine, CVaR, Drawdown Throttle, and HAR Lever: [`kronos/risk.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/risk.py) (`source-reported`).
  - Hierarchical Risk Parity & Shrunk Covariance: [`kronos/hrp.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/hrp.py), [`kronos/covariance.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/covariance.py) (`source-reported`).
  - Black-Litterman Portfolio Constructor: [`kronos/black_litterman.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/black_litterman.py) (`source-reported`).
  - Cross-Market Transfer Experimentation: [`kronos/transfer.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/transfer.py) (`source-reported`).
  - Crypto Mechanism & Leverage Contrast: [`kronos/crypto.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/crypto.py) (`source-reported`).
  - Forensic Ledger & Overfitting Diagnostics: [`kronos/forensics.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/forensics.py) (`source-reported`).
  - Empirical Findings Monograph: [`docs/FINDINGS.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/FINDINGS.md) (`source-reported`).
  - Pre-registered Experimental Specifications: [`docs/design/DESIGN16.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/design/DESIGN16.md), [`docs/design/DESIGN19.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/design/DESIGN19.md), [`docs/design/DESIGN21.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/design/DESIGN21.md) (`source-reported`).
  - Statistical Methodology Monograph: [`docs/METHODS.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/METHODS.md) (`source-reported`).
- **Primary Source Inspection:** Direct, line-by-line inspection of Python source code, synthetic unit/causality gates, pre-registered design documents, and numerical tables at commit `2e112e4e5f01a39d89121921df86ef2970e237a4`.
- **Repository Deduplication Audit:** A comprehensive audit of all existing markdown records in `alpha-strategy-research` confirmed zero prior records citing `Olivesz`, `kronos-quant`, or commit `2e112e4e5f01a39d89121921df86ef2970e237a4`.

## Economic mechanism

### Source-reported

1. **Closure of Daily Direction Timing:** An information-theoretic study of market returns (KRONOS-BITS) proved that daily directional signs carry zero forecastable mutual information ($I(\text{sign}_t; \text{forward sign}) \approx 0$ nats/day). Daily market timing is an unharvestable, noise-dominated channel. True trading edge exists only in the **forecastable magnitude/volatility channel** and risk-allocation structure.
2. **Student-t Hidden Markov Regimes vs. Gaussian Tail Hallucination:** Standard Gaussian HMMs hallucinate spurious regime switches when exposed to leptokurtic asset returns. In Monte Carlo simulations on synthetic $K=3$ worlds with fat-tailed innovations, Gaussian HMM model selection incorrectly selected $K > 3$ in 88% of seeds (frequently picking $K=5$). By implementing a Student-t HMM (t-HMM) fitted via Expectation-Conditional-Maximization (ECM) with per-state degrees of freedom $\nu_k$, fat tails are absorbed *within* states rather than triggering false regime switches. Real-data walk-forward evaluation confirms that market dynamics collapse cleanly to $K=3$ states with distinct tail behavior: Bull ($\nu \approx 17$), Volatile ($\nu \approx 3.7-4.2$, absorbing extreme jumps), and Bear ($\nu \approx 300$, approximately Gaussian).
3. **Forecast-Volatility Targeting (HAR-RV on Garman-Klass Range Variance):** Reactive volatility targeting using trailing realized standard deviation lags market vol spikes, de-risking only after losses have occurred. Heterogeneous Autoregressive Realized Volatility (HAR-RV on Corsi 2009 / Garman-Klass daily variance) decisively outperforms trailing EWMA out-of-sample (QLIKE 0.417 vs 0.511, Diebold-Mariano $-7.1$, $p < 0.001$). Driving position sizing by forward-looking 1-step HAR volatility forecasts sizes the book *ahead* of volatility expansions.
4. **Regime-Gated Multi-Factor Views with Black-Litterman on HRP Backbone:** Rather than chasing unconstrained factor timing, the system allocates capital through a hierarchical risk parity (HRP) tree-clustering covariance backbone (which handles asset collinearity cleanly), tilted by Black-Litterman shrinkage using cross-sectional factor signals (12-1 momentum, 20-day mean reversion, Blom rank-normal low-volatility) whose relative weights are dictated by the active t-HMM regime.
5. **Mechanical Crash Control:** Early-warning crash detection tests (KRONOS-CRITICAL) proved on real historical data that market crashes behave as unforecastable exogenous shocks rather than critical transitions with leading indicators ($\text{AUC} \approx +0.03$). Consequently, crash protection cannot rely on predictive exit models; it must be managed purely mechanically via rolling 252-day historical CVaR95 caps and linear drawdown throttling.
6. **Monthly Trend Harvest via Momentum Tilt (KRONOS-MOMTILT):** While daily sign information is closed, mutual information analysis (KRONOS-HARVEST) identified that 21-day trailing market momentum retains $0.021$ unharvested bits of monthly direction information. Applying a bounded $\pm 15\%$ exposure tilt conditioned on 21-day market return direction harvests this slow trend defensively, cutting exposure during structural downturns.

### Research interpretation

The strategy represents a disciplined, **risk-first composite alpha system** that avoids direction-guessing and instead harvests multi-factor risk premia conditioned on endogenous macro volatility states. The core thesis is that edge in equities is primarily an exercise in **tail and variance management**:
- Cross-sectional factor premiums (momentum vs. reversal vs. low-vol) vary across volatility regimes: momentum dominates quiet bull regimes, while mean reversion and low volatility provide defensive alpha during volatile and bear regimes.
- By decoupling portfolio risk budgeting (HRP) from factor views (Black-Litterman), the strategy prevents high-beta factor bets from dominating the risk budget.
- Forward-looking HAR sizing eliminates the whipsaw latency inherent to trailing historical volatility filters.
- Drawdown and CVaR throttling impose an asymmetrical concave payoff, preventing right-tail compounding from being wiped out by structural market drawdowns.

## Signal

The normalized execution logic follows a causal, multi-tiered architecture:

### 1. Regime Identification Engine (Student-t HMM)
- **Model:** 3-state multivariate Student-t HMM (`kronos/thmm.py`) (`source-reported`).
- **Input Features:** Demeaned market log-returns and 10-day realized volatility (`source-reported`).
- **Training & Cadence:** Minimum warmup 750 trading days (`hmm_min_train = 750`), refit every 21 trading days (`hmm_refit_every = 21`) on expanding causal historical window (`source-reported`).
- **Estimation:** Expectation-Conditional-Maximization (ECM); degrees of freedom $\nu_k \in [2.05, 300.0]$ solved via Brent's method on the digamma equation (`source-reported`).
- **State Transition Control:** Hysteresis threshold $P > 0.65$ sustained for $\ge 5$ trading days, minimum dwell 10 trading days, overridden if state probability exceeds urgent threshold $P \ge 0.90$ (`source-reported`).
- **Regime States:** State 0 = Bull, State 1 = Volatile, State 2 = Bear (`source-reported`).

### 2. Cross-Sectional Alpha Signals
Signals are computed daily at market close $t$ across all universe assets, cross-sectionally z-scored, and clipped to $[-3.0, +3.0]$ (`source-reported`):
- **Momentum Signal:** 12-1 momentum ($t-252$ to $t-21$ cumulative return, skipping trailing 21-day reversal window) (`source-reported`).
- **Mean Reversion Signal:** Negative z-score of current price relative to 20-day SMA ($-\frac{P_t - \text{SMA}_{20}}{\sigma_{20}}$) (`source-reported`).
- **Low Volatility Signal:** Negative Blom rank-normal transform of 60-day realized daily return volatility ($-\Phi^{-1}(\frac{\text{rank} - 0.375}{N + 0.25})$) (`source-reported`).
- **Regime-Conditioned Signal Blending:**
  $$\text{Composite}_t = w_{\text{mom}}(S_t) \cdot \text{Mom}_t + w_{\text{rev}}(S_t) \cdot \text{Rev}_t + w_{\text{lowvol}}(S_t) \cdot \text{LowVol}_t$$
  Weights per active regime $S_t$ (`source-reported`):
  - Bull: $w = [0.55, 0.15, 0.30]$
  - Volatile: $w = [0.20, 0.40, 0.40]$
  - Bear: $w = [0.10, 0.30, 0.60]$

### 3. Portfolio Optimization & Black-Litterman Tilt
- **Covariance Estimation:** Shrunk covariance matrix using 252-day lookback with 63-day EWMA half-life (`source-reported`).
- **Prior Backbone:** Hierarchical Risk Parity (HRP) inverse-variance tree clustering on correlation distance (`source-reported`).
- **View Injection:** Black-Litterman shrinkage with risk aversion $\delta = 2.5$, uncertainty scalar $\tau = 0.05$, view strength $\lambda = 0.30$, and shrinkage parameter $\kappa = 1.00$ (`source-reported`).
- **Position Cap:** Maximum single-asset weight capped at 12.0% ($w_i \le 0.12$) (`source-reported`).
- **Rebalance Cadence & Banding:** Full portfolio rebalance every 21 trading days (`rebalance = 21`). Target weight adjustments $|\Delta w_i| < 0.0025$ (25 bps no-trade band) are suppressed to zero to eliminate idle turnover (`source-reported`).

### 4. Dynamic Exposure, HAR Volatility Lever, and Crash Throttling
Daily portfolio exposure multiplier $E_t$ applied at $t+1$ (`source-reported`):
- **HAR Volatility Forecast Lever ($m_{\text{vol}}$):**
  1-step forward daily variance forecast $\hat{\sigma}^2_{t+1}$ generated via OLS HAR model on Garman-Klass range variance features (1-day, 5-day mean, 22-day mean), refit every 21 trading days on expanding window ($\ge 504$ days warmup) (`source-reported`):
  $$m_{\text{vol}, t} = \min\left(\frac{\sigma_{\text{target}}}{\hat{\sigma}_{\text{HAR}, t}}, \text{max\_exposure}\right)$$
  where $\sigma_{\text{target}} = 0.13$ (13% annualized volatility) and $\text{max\_exposure} = 1.50$ (1.5x leverage cap) (`source-reported`).
- **Historical CVaR95 Brake ($m_{\text{cvar}}$):**
  $$m_{\text{cvar}, t} = \min\left(\frac{\text{CVaR}_{\text{target}}}{\text{CVaR}_{95, 252\text{d}}}, 1.0\right)$$
  where $\text{CVaR}_{\text{target}} = 0.018$ (1.8% daily tail loss) (`source-reported`).
- **Linear Drawdown Throttle ($m_{\text{dd}}$):**
  Monitors current drawdown $DD_t = \frac{\text{NAV}_t}{\max_{s \le t} \text{NAV}_s} - 1.0$ (`source-reported`):
  - $DD_t \ge -0.08$: $m_{\text{dd}} = 1.00$ (full exposure).
  - $-0.20 < DD_t < -0.08$: Linear de-risking down to floor.
  - $DD_t \le -0.20$: $m_{\text{dd}} = 0.25$ (`dd_min_exp = 0.25`).
- **Momentum Directional Tilt ($m_{\text{tilt}}$):**
  $$m_{\text{tilt}, t} = 1.0 + 0.15 \cdot \text{sign}\left(\sum_{s=t-20}^t \log r_{\text{SPY}, s}\right)$$
  where $0.15$ represents a frozen $\pm 15\%$ exposure tilt (`source-reported`).
- **Final Lagged Exposure Execution:**
  $$\text{Raw}_t = m_{\text{vol}, t} \cdot \min(m_{\text{cvar}, t}, m_{\text{dd}, t}) \cdot m_{\text{tilt}, t}$$
  $$E_t = \text{clip}\left(\text{EWMA}_5(\text{Raw}_t), 0.0, 1.50\right)$$
  Applied strictly at $t+1$ as $E_t \cdot w_t$ (`source-reported`). Financing cost of 3.5% annualized is deducted daily on the levered portion $\max(E_t - 1.0, 0.0)$ (`source-reported`).

## Required data

- **Universe:** 48 liquid US large-cap equities and sector/asset ETFs (`AAPL`, `MSFT`, `NVDA`, `AMZN`, `GOOGL`, `META`, `JPM`, `BAC`, `GS`, `UNH`, `JNJ`, `PFE`, `XOM`, `CVX`, `CAT`, `HON`, `BA`, `WMT`, `PG`, `KO`, `PEP`, `MCD`, `HD`, `DIS`, `NFLX`, `CRM`, `ADBE`, `INTC`, `CSCO`, `ORCL`, `T`, `VZ`, `NEE`, `DUK`, `LIN`, `FDX`, `UPS`, `SPY`, `QQQ`, `IWM`, `DIA`, `XLF`, `XLE`, `XLK`, `XLU`, `GLD`, `TLT`, `HYG`, `LQD`) + `SPY` market benchmark (`source-reported`).
- **Venue / Asset Class:** US Cash Equities & ETFs (NYSE, NASDAQ) (`source-reported`).
- **Timeframe / Resolution:** Daily bars (`source-reported`).
- **Price Fields:** Open, High, Low, Close, Split-and-Dividend-Adjusted Close, Volume (`source-reported`).
- **Derived Fields:** Garman-Klass range variance $v_t = 0.5(\log \frac{H_t}{L_t})^2 - (2\log 2 - 1)(\log \frac{C_t}{O_t})^2$ (`source-reported`).
- **Point-in-Time & Look-Ahead Hygiene:** All estimators, parameters, covariance estimates, and factor ranks are strictly causal ($t+1$ execution uses observations $\le t$ only). Causality is formally enforced by Gate X23 and Gate X29 (`causality: max target-weight diff on shared dates = 0.00e+00`) (`source-reported`).
- **Missing Data Handling:** Assets require $\ge 95\%$ historical coverage (`min_coverage = 0.95`); forward-fill capped at 3 trading days (`max_ffill_days = 3`); returns exceeding $60\%$ single-day change clipped as bad-tick data corruptions (`source-reported`).

## Execution assumptions

- **Signal-to-Order Timing:** Decisions formed at close of day $t$; execution filled at next-day $t+1$ bar (`research-proposed next-day execution`).
- **Order Types & Execution:** Market / rebalancing orders (`research-proposed`).
- **Transaction Costs (Direct):** 1.0 bp commission + 2.0 bps half-spread across all executed turnover (`source-reported`).
- **Market Impact Model:** Square-root temporary market impact model deducted from each rebalancing trade (`source-reported`):
  $$\text{Impact}_{\text{bps}} = c \cdot \sigma_{d, i} \cdot \sqrt{\frac{|\Delta w_i|}{0.01}}$$
  where $c = 10.0$ and impact is capped at 25.0 bps per trade (`impact_cap_bps = 25.0`) (`source-reported`).
- **Leverage Financing:** 3.5% annualized interest rate charged daily on borrowed capital when portfolio exposure exceeds 1.0x (`financing_rate_ann = 0.035`) (`source-reported`).
- **Capacity Constraints:** Simulated on liquid large-cap US names ($>\$5\text{B}$ market cap, ETF volume $>\$100\text{M}$/day); research-proposed institutional capacity estimate $\approx \$250\text{M}$ without breaking impact bounds (`research-proposed`).
- **Fill Reliability:** 100% fill assumption at simulated cost-adjusted prices; no partial-fill queue modeling (`research-proposed fill model`).

## Evidence

### Source-reported

All empirical figures below are extracted directly from the verified primary codebase and monograph tables of Oliverz (`Olivesz/kronos-quant`, commit `2e112e4e5f01a39d89121921df86ef2970e237a4`, files `docs/FINDINGS.md`, `docs/design/DESIGN16.md`, `docs/design/DESIGN21.md`, and `config.py`):

1. **Full-Sample Walk-Forward Backtest (Net of All Trading Costs, Impact, and Financing):**
   - **Sample Period:** 2013-01-14 through 2026-06-04 (3,368 traded days following 750-day warmup from 2010-01-01) (`source-reported`).
   - **Performance Comparison:**
     | Configuration / Benchmark | CAGR | Sharpe Ratio | Max Drawdown | Daily CVaR95 |
     |---|---|---|---|---|
     | **KRONOS Shipped System (HAR lever + t-HMM + MomTilt)** | **11.8%** | **1.07** | **−17.9%** | **1.65%** |
     | KRONOS Joint (HAR lever + t-HMM, untilted) | 12.0% | 1.05 | −18.8% | 1.70% |
     | KRONOS V1 (HAR lever only, Gaussian HMM) | 11.7% | 1.03 | −19.4% | 1.70% |
     | KRONOS Baseline (EWMA lever, Gaussian HMM) | 10.9% | 0.95 | −21.3% | 1.76% |
     | Realized-Vol Control (Unlevered 1.0x) | 9.0% | 1.01 | −16.7% | 1.34% |
     | SPY Buy-and-Hold Benchmark | 15.0% | 0.91 | −33.7% | 2.55% |
     | Equal-Weight Basket Benchmark | 16.6% | 1.10 | −30.5% | 2.24% |

2. **Split-Half Out-of-Sample Consistency:**
   - **H1 (2013–2019):** Sharpe 1.32, CAGR +14.9% (vs. baseline Sharpe 1.26) (`source-reported`).
   - **H2 (2020–2026):** Sharpe 0.81, CAGR +8.8% (vs. baseline Sharpe 0.64) (`source-reported`).
   - The upgrades are complementary across market regimes: the HAR forecast lever provided its largest margin of safety in H2 (2020–2026 volatile markets), while the Student-t HMM engine provided its largest stability boost in H1 (2013–2019) (`source-reported`).

3. **Behavior During Acute Historical Market Stress:**
   - **2020 COVID Crash (Feb–Apr 2020):** Exposure was automatically throttled to a minimum of 0.11 (average exposure 0.53) (`source-reported`).
   - **2022 Bear Market:** Exposure throttled to a minimum of 0.37 (average exposure 1.01) (`source-reported`).
   - **SPY Drawdown $> 10\%$ Episodes:** Average exposure reduced to 0.88 vs. 1.37 during normal periods (`source-reported`).

4. **Statistical Rigor & Overfitting Forensics:**
   - **Deflated Sharpe Ratio (DSR):** DSR = 0.75 after charging the full pre-registered ledger of 185 experimental configurations ($N = 185$) (`source-reported`).
   - **Combinatorially Symmetric Cross-Validation (CSCV):** Probability of Backtest Overfitting (PBO) = 0.45 (`source-reported`).
   - **Bootstrap Confidence Interval:** Stationary bootstrap 95% confidence interval for annualized Sharpe is $[0.54, 1.52]$, excluding zero (`source-reported`).

5. **Cross-Market Transfer Out-of-Sample (Frozen Parameters, Zero Local Retuning):**
   - The US-calibrated trading system was evaluated without parameter adjustments on three distinct international market universes:
     | Market Universe | KRONOS Sharpe | Local Index Sharpe | KRONOS Max Drawdown | Local Index Max Drawdown |
     |---|---|---|---|---|
     | **Japan (Nikkei/TOPIX Large-Caps)** | **0.83** | 0.79 | **−20%** | −33% |
     | **Europe (STOXX Large-Caps)** | **0.67** | 0.59 | **−22%** | −38% |
     | **Asia-EM Large-Caps** | **0.93** | 0.30 | **−18%** | −49% |
   - Source finding: In every international market, the system retained positive Sharpe and delivered shallower drawdowns than the local market index (`source-reported`).

### Independently reproduced

Not independently reproduced. All statistics above are source-reported results extracted from Oliverz (`Olivesz/kronos-quant`, commit `2e112e4e5f01a39d89121921df86ef2970e237a4`). No execution has occurred within PyBroker or NautilusTrader.

### Negative evidence

The source author documented an extensive battery of honest negative results and falsifications:
1. **Classic Statistical Arbitrage Decay:** Avellaneda-Lee eigenportfolio pairs stat-arb lost $-1.3\%$/year (Sharpe $-0.24$) net of costs on real data, despite functioning at Sharpe 2.4 on synthetic Ornstein-Uhlenbeck test worlds, confirming post-2008 post-publication alpha decay in large-cap equities (`source-reported`).
2. **Semi-Markov Duration Models Failed:** Explicit duration-HMM (semi-Markov) tied the plain HMM out of sample (3.1669 vs. 3.1689 nats/day), showing that explicit dwell-time modeling adds zero predictive power over simple Markov transitions (`source-reported`).
3. **Random Matrix Theory (RMT) Denoising Failed:** Marchenko-Pastur spectral clipping failed to beat Ledoit-Wolf shrinkage on the 48-asset universe (realized min-variance vol 6.04% vs 5.84%), demonstrating that RMT is ineffective for moderate $N/T$ dimensions (`source-reported`).
4. **Machine Learning Ensemble Failure:** Online Hedge and fixed-share learning algorithms failed to beat hand-crafted regime weights (all tied at Sharpe $\approx 0.99$), because sleeves were heavily co-dependent through the shared HRP covariance backbone (`source-reported`).
5. **CSCV PBO Barrier:** A PBO of 0.45 confirms that the final strategy configuration cannot be statistically certified as superior over sibling configurations in the search family; its legitimacy rests on synthetic gating, structural economic mechanisms, and cross-market transfer rather than in-sample point maximization (`source-reported`).
6. **No Raw Return Alpha:** The strategy's CAGR (11.8%) is substantially lower than SPY buy-and-hold (15.0%) and equal-weight equity (16.6%). The strategy generates zero directional return alpha; its entire contribution is risk reduction, drawdown truncation, and Sharpe expansion (`source-reported`).

## Falsification plan

To falsify the economic hypothesis and operational validity of the KRONOS strategy, execute the following pre-registered empirical tests:

1. **Walk-Forward Out-of-Sample Holdout (2026–2028):**
   - Evaluate performance on fresh out-of-sample data post June 2026 without parameter recalibration.
   - `Research-defined falsification threshold:` Annualized net Sharpe ratio $< 0.50$ or maximum drawdown $> -25.0\%$ over a rolling 2-year evaluation window.
   - *Action on failure:* Reject the strategy as an overfitted regime artifact.
2. **Volatility Forecasting Ablation (HAR-RV vs. Trailing Realized Volatility):**
   - Replace the 1-step HAR-RV forecast engine with a simple trailing 21-day realized standard deviation.
   - `Research-defined falsification threshold:` If trailing realized volatility achieves a higher net Sharpe or lower maximum drawdown than HAR-RV, falsify the core thesis that forecast-volatility sizing provides superior risk-timing.
   - *Action on failure:* Decommission the HAR module and strip model complexity.
3. **Student-t HMM Regime Ablation:**
   - Compare the Student-t HMM against: (a) static equal factor weighting ($w = [\frac{1}{3}, \frac{1}{3}, \frac{1}{3}]$); and (b) a Gaussian HMM baseline.
   - `Research-defined falsification threshold:` If the static weighting baseline achieves an out-of-sample Sharpe within 0.05 of the t-HMM engine across a full 5-year cycle, falsify the regime-conditioned factor rotation hypothesis.
   - *Action on failure:* Eliminate regime-switching state logic and adopt static factor risk parity.
4. **Transaction Cost & Market Impact Stress Test:**
   - Scale transaction fees from 1.0 bp / 2.0 bps to 5.0 bps commission and 10.0 bps spread, scaling market impact coefficient $c$ from 10.0 to 30.0.
   - `Research-defined falsification threshold:` Net Sharpe ratio collapsing below $0.40$ indicates that the 21-day rebalancing turnover and HRP adjustments cannot withstand realistic institutional slippage.
   - *Action on failure:* Enlarge the no-trade band from 25 bps to 100 bps or increase the rebalancing cadence to 63 trading days.
5. **Placebo Shuffled Return Test:**
   - Permute the cross-sectional asset return vectors while preserving market-level volatility and SPY momentum.
   - `Research-defined falsification threshold:` If the factor-tilted portfolio fails to outperform a randomized cross-sectional allocation by at least 1.5 standard errors, reject factor-view efficacy.

## Crypto portability

- **Classification:** `Adapted` / `Unproven` (`research-proposed`).
- **Source-Demonstrated Cross-Asset Law Transfer (KRONOS-CRYPTO):**
  The author evaluated the underlying market-structure laws on 10 crypto majors (`BTC-USD`, `ETH-USD`, `XRP-USD`, `LTC-USD`, `BCH-USD`, `ADA-USD`, `DOGE-USD`, `LINK-USD`, `XLM-USD`, `ETC-USD`) using daily OHLC from 2017 to 2026 (`source-reported`).
- **The Critical Leverage Effect Inversion:**
  - In equities, the leverage effect is universally negative (returns and future volatility correlate at $-0.041$, $z = 4.06$; price drops cause leverage to rise, inducing volatility spikes) (`source-reported`).
  - **In crypto, the leverage effect cleanly INVERTS to positive $+0.031$**, with 8 of 10 coins individually positive (`DOGE` $+0.078$, `XLM` $+0.059$, `ADA` $+0.042$, `BCH` $+0.040$, `LTC` $+0.033$; only `BTC` $-0.043$ and `ETH` $-0.019$ retain negative signs) (`source-reported`).
  - *Mechanism:* Crypto lacks traditional corporate financial leverage and institutional margin call cascade mechanics. Instead, crypto volatility is driven by retail FOMO and aggressive leveraged speculative buying where explosive rallies—not crashes—induce the largest volatility explosions (`source-reported`).
- **Portability Implications for Strategy Architecture:**
  1. *Direct Porting is Invalid:* Applying the equity HAR-RV volatility lever to crypto will cause the strategy to aggressively de-risk during vertical bull runs (because volatility surges as price climbs), severely handicapping upside capture (`research-proposed`).
  2. *Regime Inversion:* Bull regimes in crypto exhibit high realized volatility, contrary to quiet equity bull markets (`research-proposed`).
  3. *Perpetual Funding Rate Drag:* Maintaining directional short or levered exposures in crypto perpetuals incurs variable 8-hour funding rates, which are absent in equity cash markets (`research-proposed`).
  4. *24/7 Session Structure:* Absence of weekend/overnight closing boundaries requires continuous order-book execution rather than discrete T+1 day-boundary rebalancing (`research-proposed`).

## Limitations

1. **Survivorship Bias in Equity Universe:** The 48-asset universe consists of large-cap US equities and ETFs liquid as of 2026, introducing historical survivorship conditioning (`source-reported`).
2. **Elevated Probability of Backtest Overfitting (PBO = 0.45):** Over 185 experimental configurations were logged in the project trial ledger. Although DSR remains 0.75, a PBO of 0.45 confirms substantial selection hazard across parameter variants (`source-reported`).
3. **Underperformance vs. Passive Benchmark on Raw Return:** The strategy sacrifices raw compounding (CAGR 11.8% vs. SPY 15.0%) in exchange for drawdown mitigation (-17.9% vs. -33.7%). Investors evaluated solely on unadjusted total return will underperform the benchmark (`source-reported`).
4. **HMM Lag & Hysteresis Latency:** The 5-day hysteresis requirement and 10-day minimum dwell time prevent state flickering but introduce delayed detection during rapid market transitions (`source-reported`).
5. **Synthetic Fallback Dependence:** Portions of the testing suite rely on seeded synthetic Student-t Markov jump models; real market dislocations may exhibit non-stationary multi-point jump dynamics outside the simulated bracket (`research-proposed`).

## Implementation status

No implementation has been conducted in `nautilus-quant-system`, PyBroker, or NautilusTrader. This document is a normalized research capture only.

## Adoption boundary

This record is research material only. Its presence in this repository does not constitute:
- Verified production alpha;
- Approval for portfolio deployment;
- Permission to trade on paper, demo/testnet, or live trading accounts.

Any progression to backtesting, paper execution, or live capital allocation requires independent review, signal parity verification, and formal approval within the Nautilus quantitative governance framework.

## Related Wiki records

- `[[quant/hierarchical-risk-parity-machine-learning-portfolio-allocation]]`
- `[[quant/regime-switching-hidden-markov-models-asset-allocation]]`
- `[[quant/volatility-targeting-risk-budgeting-drawdown-control]]`
- `[[quant/black-litterman-bayesian-shrinkage-portfolio-optimization]]`
- `[[quant/har-rv-high-frequency-realized-volatility-forecasting]]`

## Sources

1. Oliverz (`Olivesz`). *"KRONOS: Regime-aware quantitative alpha platform & market-microstructure research lab"*. Public GitHub repository, commit `2e112e4e5f01a39d89121921df86ef2970e237a4`, published and committed September 2026.
   - Repository URL: [https://github.com/Olivesz/kronos-quant](https://github.com/Olivesz/kronos-quant)
   - Commit Tree: [https://github.com/Olivesz/kronos-quant/tree/2e112e4e5f01a39d89121921df86ef2970e237a4](https://github.com/Olivesz/kronos-quant/tree/2e112e4e5f01a39d89121921df86ef2970e237a4)
   - Core Trading System: [`kronos/trade.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/trade.py)
   - Configuration Specification: [`config.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/config.py)
   - Student-t HMM Implementation: [`kronos/thmm.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/thmm.py)
   - Volatility Lab & HAR Engine: [`kronos/vollab.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/vollab.py)
   - Risk & Sizing Engine: [`kronos/risk.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/risk.py)
   - Cross-Market Transfer: [`kronos/transfer.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/transfer.py)
   - Crypto Mechanism & Leverage Study: [`kronos/crypto.py`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/kronos/crypto.py)
   - Findings Monograph: [`docs/FINDINGS.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/FINDINGS.md)
   - Statistical Methodology: [`docs/METHODS.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/METHODS.md)
   - Performance Program Pre-registration: [`docs/design/DESIGN16.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/design/DESIGN16.md)
   - Momentum Tilt Pre-registration: [`docs/design/DESIGN21.md`](https://github.com/Olivesz/kronos-quant/blob/2e112e4e5f01a39d89121921df86ef2970e237a4/docs/design/DESIGN21.md)
