---
schema: strategy-research-record-v1
title: "Moving-Band Statistical Arbitrage via Convex-Concave Optimization and Dynamic Markowitz Basket Allocation: Multi-Asset Spread Discovery and Second-Order Cone Portfolio Management"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - moving-band
  - convex-optimization
  - convex-concave-procedure
  - markowitz
  - portfolio-management
  - pairs-trading
  - mean-reversion
  - market-neutral
status: research-only
confidence: high
source_as_of: 2024-12-03
sources:
  - "Kasper Johansson, Thomas Schmelzer, Stephen Boyd, 'A Markowitz Approach to Managing a Dynamic Basket of Moving-Band Statistical Arbitrages', arXiv:2412.02660v1 [econ.EM], December 3, 2024. https://arxiv.org/abs/2412.02660"
  - "Kasper Johansson, Thomas Schmelzer, Stephen Boyd, 'Finding Moving-Band Statistical Arbitrages via Convex-Concave Optimization', arXiv:2402.08108v1 [econ.EM], February 12, 2024. https://arxiv.org/abs/2402.08108"
  - "cvxgrp/cvxstatarb, GitHub repository, commit 7fa380372bcbc4d64a8603ffa88afd718d619780, May 2025. https://github.com/cvxgrp/cvxstatarb"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Moving-Band Statistical Arbitrage via Convex-Concave Optimization and Dynamic Markowitz Basket Allocation: Multi-Asset Spread Discovery and Second-Order Cone Portfolio Management

## Provenance

- **Primary Theoretical & Discovery Source:** Kasper Johansson (Stanford University), Thomas Schmelzer (Abu Dhabi Investment Authority), and Stephen Boyd (Stanford University), *"Finding Moving-Band Statistical Arbitrages via Convex-Concave Optimization"*, arXiv preprint `arXiv:2402.08108v1 [econ.EM]`, submitted February 12, 2024.
  - Canonical arXiv Abstract: [https://arxiv.org/abs/2402.08108](https://arxiv.org/abs/2402.08108)
  - Full Text HTML: [https://arxiv.org/html/2402.08108v1](https://arxiv.org/html/2402.08108v1)
- **Primary Portfolio Management & Markowitz Source:** Kasper Johansson (Stanford University), Thomas Schmelzer (Abu Dhabi Investment Authority), and Stephen Boyd (Stanford University), *"A Markowitz Approach to Managing a Dynamic Basket of Moving-Band Statistical Arbitrages"*, arXiv preprint `arXiv:2412.02660v1 [econ.EM]`, submitted December 3, 2024.
  - Canonical arXiv Abstract: [https://arxiv.org/abs/2412.02660](https://arxiv.org/abs/2412.02660)
  - Full Text HTML: [https://arxiv.org/html/2412.02660v1](https://arxiv.org/html/2412.02660v1)
- **Canonical Public Code Implementation:** Stanford University Convex Optimization Group (`cvxgrp`), repository `cvxstatarb` on GitHub.
  - Repository URL: [https://github.com/cvxgrp/cvxstatarb](https://github.com/cvxgrp/cvxstatarb)
  - Immutable Verified Commit SHA: `7fa380372bcbc4d64a8603ffa88afd718d619780` (as of May 21, 2025).
  - Exact Implementation Paths Inspected: `cvx/stat_arb/ccp.py`, `experiments/backtest.py`, `experiments/utils.py`.
- **Pre-Write Deduplication & Identity Verification:** An exhaustive search of all 370+ markdown records across `alpha-strategy-research` confirmed zero existing records matching `2402.08108`, `2412.02660`, `cvxstatarb`, `Johansson`, `Schmelzer`, `Stephen Boyd`, or the Moving-Band Statistical Arbitrage (MBSA) formulation. Existing statistical arbitrage records in the repository rely on classical cointegration pairs, high-frequency order-flow signals, graph Laplacian clustering (`SPONGE`), or deep LSTM residual forecasting; none formulate the non-convex variance-maximization moving-band discovery problem via CCP, nor the unified Second-Order Cone Programming (SOCP) Markowitz basket manager with iterated EWMA price-deviation risk modeling.

## Economic mechanism

### Source-reported

1. **Mean Reversion in Multi-Asset Price Bands:** Classical statistical arbitrage (Gatev et al. 2006; Avellaneda & Lee 2010) typically focuses on pairs of assets or spreads defined by rigid econometric cointegration tests (Engle & Granger 1987; Johansen 2000) or distance metrics. However, distance minimization fails because it searches for pairs that do not move relative to each other, whereas a profitable statistical arbitrage crucially requires high variance around its equilibrium. Furthermore, fixed-band spreads often suffer structural regime breaks where the long-term equilibrium shifts, leading to prolonged drawdowns and capital lockup.
2. **Moving-Band Generalization (MBSA):** Johansson, Schmelzer, and Boyd (2024) introduce the Moving-Band Statistical Arbitrage (MBSA), where the spread midpoint $\mu_t$ is permitted to drift as a trailing moving average of the portfolio's own price history ($\mu_t = \frac{1}{M}\sum_{\tau=t-M+1}^t p_\tau$). This integrates the intuition of technical Bollinger bands into an endogenously optimized multi-asset portfolio, allowing the strategy to adapt to slow macroeconomic drifts, secular inflation, or structural sector re-ratings while harvesting short-term mean-reverting oscillations around the moving band.
3. **Variance Maximization as Profit Maximization:** The authors prove analytically that under a simple linear trading policy $q_t = \mu_t - p_t$, the trading profit over horizon $T$ is mathematically lower-bounded by one-half of the cumulative squared price differences:
   $$\text{Profit} \ge \frac{1}{2}\left(\sum_{t=2}^T (p_t - p_{t-1})^2 - 1\right)$$
   Therefore, maximizing the volatility $\sum_{t=2}^T (p_t - p_{t-1})^2$ subject to the portfolio price remaining strictly within $[-1, 1]$ of its moving midpoint directly maximizes trading profits.
4. **Decoupled Portfolio Management (Markowitz Basket Allocation):** In traditional statistical arbitrage, each pair is traded in isolation or equal-weighted. Johansson et al. (2024b) decouple discovery from portfolio management, showing that an aggregate dynamic basket of $K_t$ active MBSAs can be managed simultaneously through a single multi-period convex optimization problem. This framework explicitly models cash neutrality ($p_t^T q = 0$), regulatory shorting collateral ($c \ge (\eta - 1) P_t^T h_-$), quadratic transaction cost penalties, short-borrow fees, and a novel second-order cone risk limit based on price deviations from midpoints rather than unhedged asset returns.

### Research interpretation

1. **Convex-Concave Procedure as Non-Convex Search:** Finding an MBSA requires maximizing a convex quadratic objective subject to convex box constraints on price deviations and an $\ell_1$ leverage budget. This is a non-convex difference-of-convex problem. The sequential linearizations in CCP create a disciplined sequence of Linear Programs (LPs) that converge rapidly to locally optimal sparse portfolios without requiring combinatorial brute-force search over $\binom{n}{k}$ asset subsets.
2. **Endogenous Factor Neutralization via $\ell_1$ Regularization:** The leverage constraint $|s|^T \bar{P} \le L$ acts as a weighted $\ell_1$ norm penalty. Because the optimizer seeks high variance within a narrow band, it naturally pairs assets with offsetting common factor exposures (market beta, sector, momentum) while leaving idiosyncratic, high-frequency mean-reverting residuals intact.
3. **De-risking via Trailing Midpoint Decay:** Unlike fixed-band cointegration where an asset pair that diverges permanently generates catastrophic martingale-style losses, the trailing $M$-period midpoint dynamically chases trending price moves. If a fundamental break occurs, the moving midpoint catches up to the new price level over $M$ periods, automatically compressing the alpha signal $\alpha_t = \mu_t - p_t$ toward zero and forcing the Markowitz optimizer to exit the position smoothly.
4. **Capacity & Microstructure Friction Bottleneck:** While the strategy achieves a reported Sharpe ratio of 1.61 across 11 years with zero negative annual returns, it requires an annual turnover of 136 (daily turnover ~50% of portfolio NAV). The entire empirical alpha hinges on whether effective execution costs (bid-ask spread + market impact) remain below the short-term mean-reversion amplitude.

## Signal

The strategy operates in two distinct, decoupled phases: (1) periodic offline MBSA discovery via CCP, and (2) daily online portfolio rebalancing via Markowitz Second-Order Cone Programming (SOCP).

### Phase 1: MBSA Discovery via Convex-Concave Procedure (`source-reported`)

- **Formation Cadence:** Every 21 trading days (`source-reported`), evaluated over a rolling lookback window of historical daily adjusted closing prices $P_\tau \in \mathbb{R}_{++}^n$ for $\tau = 1, \dots, T$.
- **Band Midpoint Formulation:** Moving midpoint with memory $M = 21$ trading days (`source-reported`):
  $$\mu_t = \frac{1}{M} \sum_{\tau = t - M + 1}^t p_\tau = \frac{1}{M} \sum_{\tau = t - M + 1}^t s^T P_\tau$$
- **Primary Non-Convex Optimization Problem:**
  $$\begin{array}{ll}
  \text{maximize} & f(p) = \sum_{t=2}^T (p_t - p_{t-1})^2 \\
  \text{subject to} & -1 \le p_t - \mu_t \le 1, \quad t = 1, \dots, T \\
  & p_t = s^T P_t, \quad t = 1, \dots, T \\
  & |s|^T \bar{P} \le L \\
  & \mu_t = \frac{1}{M} \sum_{\tau = t - M + 1}^t p_\tau, \quad t = 1, \dots, T
  \end{array}$$
  where $\bar{P} = \frac{1}{T}\sum_{t=1}^T P_t$ is the asset price mean vector, and $L = \$100$ is the leverage budget (`source-reported`).
- **Convex-Concave Procedure (CCP) Iteration:**
  At iteration $k$, the convex quadratic objective $f(p)$ is replaced with its affine lower bound $\hat{f}(p; p^k) = \nabla f(p^k)^T p + \text{const}$, where:
  $$(\nabla f(p^k))_t = \begin{cases}
  2(p_1^k - p_2^k), & t = 1 \\
  2(2p_t^k - p_{t-1}^k - p_{t+1}^k), & t = 2, \dots, T - 1 \\
  2(p_T^k - p_{T-1}^k), & t = T
  \end{cases}$$
  The resulting problem is a Linear Program (LP) solved iteratively until $|obj_{\text{new}} - obj_{\text{old}}| / obj_{\text{old}} \le 10^{-3}$ or a maximum of 5 iterations per restart (`source-reported` from `cvxstatarb`).
- **Initialization:** 10 random restarts per cycle with $s^1 \sim \text{Uniform}(0, 1)^n$ (`source-reported`).
- **Two-Pass Polish & Sparsity Pruning:**
  Upon convergence of the first pass, assets whose capital allocation is negligible are identified:
  $$|s_i| \bar{P}_i \le 0.05 \cdot |s|^T \bar{P}$$
  All such assets are pruned ($s_i = 0$), and the CCP optimization is re-solved over the surviving subset of non-zero assets (`source-reported` from `cvxstatarb`).
- **MBSA Alpha Signal:** For active MBSA $k$, the instantaneous alpha at day $t$ is:
  $$\alpha_t^{(k)} = \mu_t^{(k)} - p_t^{(k)}$$
  If $\alpha_t^{(k)} > 0$, the MBSA price is below its moving midpoint (long expected return); if $\alpha_t^{(k)} < 0$, it is above its moving midpoint (short expected return).

### Phase 2: Dynamic Basket Markowitz Allocation (`source-reported`)

- **Rebalancing Cadence:** Daily rebalancing (`source-reported`).
- **Universe of Active MBSAs:** At day $t$, $K_t$ MBSAs are active.
- **MBSA Lifetime & Decommissioning:** Each MBSA is retained in the active basket for a maximum lifetime of 500 trading days (`source-reported`). After 500 trading days, the MBSA is phased out linearly over the subsequent $l = 21$ trading days by multiplying its position limit by:
  $$\text{multiplier}_t^{(k)} = 1 - \frac{t - 500}{21}, \quad \text{for } t \in [501, 521]$$
- **Daily Markowitz Optimization Problem (SOCP):**
  $$\begin{array}{ll}
  \text{maximize}_{h, q, c} & \alpha_t^T q - \gamma^{\text{trade}} (\kappa_t^{\text{trade}})^T |h - h_{t-1}| - \gamma^{\text{short}} (\kappa_t^{\text{short}})^T (-h)_+ - \gamma^{\text{arb-to-asset}} \|P_t \circ (h - S_t q)\|_1 \\
  \text{subject to} & c = c_{t-1} + p_t^T q_{t-1} \\
  & p_t^T q = 0 \quad (\text{cash-neutrality}) \\
  & c \ge (\eta - 1) P_t^T (h)_- \quad (\text{collateral constraint}) \\
  & |q_k| |(p_t)_k| \le \xi_t^{(k)} c, \quad k = 1, \dots, K_t \quad (\text{MBSA size limit}) \\
  & \|\Sigma_t^{1/2} q\|_2 \le \frac{\sigma^{\text{tar}}}{\sqrt{250}} c \quad (\text{SOCP risk limit})
  \end{array}$$
  where:
  - $q \in \mathbb{R}^{K_t}$ is the MBSA allocation vector (units: MBSA shares).
  - $h \in \mathbb{R}^n$ is the underlying asset holding vector (units: stock shares).
  - $S_t = [s^{(1)}, \dots, s^{(K_t)}] \in \mathbb{R}^{n \times K_t}$ is the MBSA-to-asset composition matrix.
  - $c \in \mathbb{R}_{++}$ is the cash collateral account in USD.
  - $\alpha_t \in \mathbb{R}^{K_t}$ is the vector of MBSA alphas ($\mu_t - p_t$).
  - $\kappa_t^{\text{trade}}$ is half the asset bid-ask spread; $\gamma^{\text{trade}} = 1.0$ (`source-reported`).
  - $\kappa_t^{\text{short}}$ is the asset borrow rate (0.5% annualized proxy); $\gamma^{\text{short}} = 1.0$ (`source-reported`).
  - $\eta = 1.0$ (or $2.02$ for 102% regulatory margin); baseline paper uses $\eta = 1.0$ (`source-reported`).
  - $\xi = 1.0$ common size limit (`source-reported`).
  - $\sigma^{\text{tar}} = 10\%$ annualized target risk (`source-reported`).
  - $\gamma^{\text{arb-to-asset}} = 0.1$ soft relaxation penalty parameter (`source-reported` from `cvxstatarb`).

### Phase 3: Short-Term Deviation Covariance Model ($\Sigma_t$) (`source-reported`)

- **Centered Asset Prices:** $\tilde{P}_t = P_t - \bar{P}_t$, where $\bar{P}_t$ is the 21-day rolling mean of asset prices.
- **Iterated EWMA (IEWMA) Model:** Covariance $\Sigma_t^P$ of centered prices is estimated using IEWMA with:
  - Volatility half-life: 125 trading days (`source-reported`).
  - Correlation half-life: 250 trading days (`source-reported`).
  - Risk smoothing: 250-day half-life EWMA on covariance entries to eliminate turnover induced by risk model noise (`source-reported`).
- **MBSA-Level Covariance Projection:**
  $$\Sigma_t = S_t^T \Sigma_t^P S_t$$
  If $\Sigma_t$ is not positive semi-definite due to numerical issues, project onto PSD cone: $\Sigma_{\text{proj}} = V \text{diag}(\max(\lambda_i, 10^{-6})) V^T$ (`source-reported` from `cvxstatarb`).

## Required data

- **Universe:** US Equities constituent universe (CRSP US Stock Database via WRDS). 15,405 historical equities from January 4, 2010 to December 30, 2023 (3,282 trading days).
- **Timeframe:** Daily adjusted closing prices (split- and dividend-adjusted).
- **Point-in-Time Availability:**
  - Asset prices $P_t$: available at market close $t$; executed at close/next open.
  - Active MBSA matrix $S_t$: re-estimated every 21 days using strictly historical training data (no look-ahead).
  - Rolling mean $\bar{P}_t$ and midpoint $\mu_t$: strictly trailing ($t - M + 1$ to $t$).
  - Missing Data: Inactive or delisted assets dropped via `.dropna(axis=1)` prior to CCP optimization (`source-reported` from `cvxstatarb`).
- **Execution Cost Data:**
  - Bid-ask spread: observed daily bid and ask prices from CRSP (`source-reported`).
  - Short borrow fee: 0.5% annualized proxy baseline (`source-reported`); tested up to 10% annualized.

## Execution assumptions

- **Execution Pricing:** Asset purchases executed at the ask price ($P_t^{\text{mid}} + \frac{1}{2}\text{spread}$); asset sales executed at the bid price ($P_t^{\text{mid}} - \frac{1}{2}\text{spread}$) (`source-reported`).
- **Fill Timing:** Same-day closing prices in daily discrete backtest simulation (`source-reported`). A 1-bar execution delay is an essential `research-proposed` robustness check.
- **Market Impact:** Linear bid-ask spread cost included; nonlinear square-root price impact is omitted by the primary source (`source-reported provenance gap`).
- **Shorting Frictions:** Short positions incur 0.5% annualized borrow fees, deducted daily from cash collateral (`source-reported`).
- **Collateral & Leverage Model:** Cash-neutral portfolio ($p_t^T q = 0$). Portfolio Net Asset Value (NAV) equals cash balance $V_t = c_t$.
- **Early NAV Termination Rule:** If the portfolio NAV falls below 50% of initial investment ($V_t < 0.5 C_0$), all positions are immediately liquidated to protect capital and prevent uncollateralized insolvency (`source-reported`).

## Evidence

### Source-reported

All quantitative figures below trace directly to Johansson, Schmelzer, and Boyd (`arXiv:2402.08108v1` and `arXiv:2412.02660v1`, 2024), evaluated on 15,405 US stocks from January 2010 to December 2023:

#### 1. Single MBSA Discovery Performance (Johansson et al., arXiv:2402.08108v1)

Across 1,270 CCP optimization solves evaluated over rolling out-of-sample periods (7 months per MBSA, $T^{\max}=125$, $T^{\text{exit}}=21$):

| Metric | Moving-Band Stat-Arbs (MBSA) | Fixed-Band Stat-Arbs (Baseline) |
| :--- | :--- | :--- |
| **Unique Stat-Arbs Found** | **712** | 545 |
| **Assets per Stat-Arb (Median)** | **5** (range: 1–10) | 6 (range: 3–9) |
| **Active Stat-Arbs at any time (Median)**| **40** | 17 |
| **Early Liquidation Rate ($V_t < 0.5 C_0$)** | **0.4% (3 out of 712)** | 4.8% (26 out of 545) |
| **Fraction of Profitable Arbs** | **70%** | 70% (Table 1) / 63% (Text) |
| **Annualized Return (Average)** | **15%** | 10% |
| **Annualized Return (Median)** | **12%** | 18% |
| **Annualized Volatility (Average)** | **20%** | 32% |
| **Annualized Volatility (Median)** | **15%** | 21% |
| **Annualized Sharpe Ratio (Average)** | **0.84** | 0.79 |
| **Annualized Sharpe Ratio (Median)** | **0.88** | 1.04 |
| **Maximum Drawdown (Average)** | **12%** | 15% |
| **Maximum Drawdown (Median)** | **9%** | 10% |

#### 2. Dynamically Managed Basket Performance (Johansson et al., arXiv:2412.02660v1)

Full Markowitz SOCP portfolio simulation over the 11-year evaluation period (Table 1 & Table 2):

| Metric | MBSA Portfolio (Dynamic Basket) | S&P 500 Market Benchmark (Risk-Matched) |
| :--- | :--- | :--- |
| **Average Annual Return** | **19%** | 11% |
| **Annual Volatility** | **12%** | 12% |
| **Annualized Sharpe Ratio** | **1.61** | 0.66 |
| **Annual Turnover** | **136** (daily ~50%) | N/A |
| **Maximum Drawdown** | **15%** | N/A |
| **Active Return** | **8%** | Baseline |
| **Active Risk** | **20%** | Baseline |
| **Residual Return (Alpha)** | **18%** | 0% |
| **Residual Risk** | **11%** | 0% |
| **Market Beta ($\beta$)** | **11%** | 100% |
| **Information Ratio** | **1.53** | Baseline |
| **Market Correlation (EWMA 250d)**| **15%** | 100% |
| **90% MBSA / 10% SPX Blend Sharpe**| **1.66** | 0.66 |
| **Calendar Year Consistency** | **11 of 11 positive years (100%)** | 9 of 11 positive years (81.8%) |
| **Outperformed Market** | **8 of 11 years (72.7%)** | N/A |

### Independently reproduced

`Not independently reproduced.` The mathematical optimization formulation and simulation pipeline are fully inspectable in the public `cvxgrp/cvxstatarb` repository (commit `7fa380372bcbc4d64a8603ffa88afd718d619780`), but full WRDS CRSP replication has not been executed within our internal research environment.

### Negative evidence

1. **Severe Turnover Drag:** The average annual turnover of 136 means that approximately 50% of the entire fund NAV is traded every single day. If bid-ask spreads widen (e.g. during liquidity crises or outside mega-caps), execution friction will rapidly erode the 19% gross return.
2. **Fixed-Band Failure Mode:** In the baseline fixed-band formulation, 4.8% of all generated stat-arbs hit the catastrophic -50% NAV early termination barrier due to persistent structural drift, illustrating that naive cointegration spreads without moving midpoints face severe tail risk.
3. **In-Sample Selection Optimism:** The authors note that candidate validation (splitting training data into train/test before trading) and sector clustering did not improve performance. However, because CCP maximizes historical sample variance over trailing windows, some discovered multi-asset combinations may reflect in-sample data mining rather than economic cointegration.
4. **Non-Convex Local Minima:** Because CCP is sensitive to initialization, different random seeds produce different MBSA sets, creating dispersion in portfolio composition.

## Falsification plan

1. **Next-Day Execution Lag Stress Test:** The primary paper assumes execution at closing prices simultaneous with signal calculation. Test with orders executed at the open of day $t+1$ (1-bar lag) or VWAP over $[t+1_{\text{open}}, t+1_{\text{close}}]$.
   - `research-defined falsification threshold`: Annualized Sharpe ratio dropping below 0.75 or net return turning negative after a 1-bar execution delay falsifies tradability.
2. **Turnover & Bid-Ask Spread Stress Multiplier:** Double the effective half-spread $\kappa_t^{\text{trade}}$ from observed historical values to simulate conservative institutional market impact (e.g. 10 bps to 25 bps round-trip).
   - `research-defined falsification threshold`: Strategy Net Sharpe collapsing below 0.50 or total transaction costs exceeding 80% of gross profit falsifies the economic viability of daily rebalancing.
3. **Random Asset Placebo / Shuffled Price Test:** Run the CCP solver on randomly paired, permuted asset time series where cross-correlations are broken while marginal variances are preserved.
   - `research-defined falsification threshold`: If the placebo MBSA basket achieves an out-of-sample Sharpe exceeding 0.60, the CCP solver's apparent edge is an artifact of over-fitting high-dimensional noise.
4. **Subperiod & Crisis Regime Stability Test:** Evaluate performance across distinct market regimes: 2011 European Debt Crisis, 2015-2016 Commodity Slump, 2018 Volmageddon/Q4 selloff, 2020 COVID Crash, and 2022 Fed Rate Hike Cycle.
   - `research-defined falsification threshold`: Maximum drawdown exceeding 25% or more than 2 consecutive negative calendar quarters falsifies regime resilience.
5. **Ablation of Iterated EWMA Deviation Risk Model:** Replace the short-term price deviation covariance $\Sigma_t = S_t^T \Sigma_t^P S_t$ with a standard static asset-return covariance matrix.
   - `research-defined falsification threshold`: If the standard return covariance produces lower turnover-adjusted Sharpe or higher drawdowns, the price-deviation risk model is confirmed as an active contributor to performance.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`. The underlying mathematical mechanics of MBSA discovery via CCP and dynamic Markowitz basket management originate strictly from US equities research and have not been demonstrated by the authors in crypto assets.
- **Continuous 24/7 Market Dynamics:** Unlike equities with discrete 16:00 EST market closes, crypto trades continuously. The 21-day rolling window must be mapped to hourly or 24-hour UTC snapshots. High-volatility weekend regimes with fragmented liquidity could destabilize moving midpoints.
- **Perpetual Futures Funding Friction:** In crypto perpetuals, holding short positions provides funding income during bull runs (positive funding rate) or costs funding during bear runs. The short holding cost parameter $\kappa_t^{\text{short}}$ must dynamically ingest 8-hour funding rates:
  $$\kappa_t^{\text{funding}} = \text{Funding Rate}_t \times P_t$$
- **High Friction & Liquidity Fragmentation:** Given the strategy's extreme turnover (136x per year), crypto taker fees (typically 2 to 5 bps) would completely erase gross alpha. The strategy could only be feasible in crypto if executed strictly via passive maker orders with negative or zero maker fee tiers.
- **Basis & Cointegration Viability:** Natural multi-asset MBSA candidates in crypto include:
  - Layer-1 ecosystems (e.g., BTC, ETH, SOL, AVAX basket);
  - Liquid Staking Tokens vs. Native Tokens (e.g., stETH, wstETH, cbETH vs. ETH);
  - Perpetual vs. Spot basis spreads across CEX venues (Binance, Bybit, OKX).

## Limitations

- `not independently reproduced`: Primary source results rely on WRDS CRSP equities data; internal verification in `nautilus-quant-system` is not yet performed.
- `high turnover dependency`: Annual turnover of 136 makes net performance exceptionally fragile to execution slippage and exchange fee schedule changes.
- `market impact omission`: Neither the paper nor the code incorporates a non-linear market impact model (e.g. Almgren-Chriss or square-root law).
- `unproven in crypto`: Multi-asset MBSA behavior under 24/7 continuous trading, funding rate shocks, and crypto exchange liquidation cascades remains unverified.
- `non-convex local optimality`: CCP guarantees convergence only to a local optimum; results depend on the initial random seed.

## Implementation status

- `not-implemented`: This research capture does not modify `nautilus-quant-system`, create PyBroker/Nautilus strategy families, or authorize paper, testnet, or live trading.
- All mathematical rules and parameters documented above reflect direct extraction from Johansson, Schmelzer, and Boyd (arXiv:2402.08108v1, arXiv:2412.02660v1) and Stanford CVX group's `cvxstatarb` codebase.

## Adoption boundary

- `status`: `research-only`
- `adoption`: `not-approved`
- `approval_scope`: `research-only`
- Research capture is strictly separated from trading authorization. This strategy is staged for intake review and potential synthetic hypothesis generation; it is not approved for live deployment, capital allocation, or broker execution.

## Related Wiki records

- `[[quant/attention-factors-statistical-arbitrage-residual-portfolios-2026-09-02]]`
- `[[quant/foreign-exchange-spatiotemporal-graph-statistical-arbitrage-2026-09-02]]`
- `[[quant/gaussian-boson-sampling-asset-clustering-statistical-arbitrage-2026-09-02]]`
- `[[quant/microstructure-mean-reversion-optimal-symmetric-band-waiting-option-2026-09-02]]`
- `[[quant/crypto-eth-fiat-bucket-market-neutral-pairs-2026-08-31]]`
- `[[quant/strategy-research-record-spec-v1]]`

## Sources

1. **Kasper Johansson, Thomas Schmelzer, and Stephen Boyd**, *"Finding Moving-Band Statistical Arbitrages via Convex-Concave Optimization"*, arXiv preprint `arXiv:2402.08108v1 [econ.EM]`, February 12, 2024. [https://arxiv.org/abs/2402.08108](https://arxiv.org/abs/2402.08108)
2. **Kasper Johansson, Thomas Schmelzer, and Stephen Boyd**, *"A Markowitz Approach to Managing a Dynamic Basket of Moving-Band Statistical Arbitrages"*, arXiv preprint `arXiv:2412.02660v1 [econ.EM]`, December 3, 2024. [https://arxiv.org/abs/2412.02660](https://arxiv.org/abs/2412.02660)
3. **Stanford University Convex Optimization Group (`cvxgrp`)**, *"cvxstatarb: Statistical Arbitrage via Convex Optimization"*, GitHub public repository, commit SHA `7fa380372bcbc4d64a8603ffa88afd718d619780`, May 21, 2025. [https://github.com/cvxgrp/cvxstatarb](https://github.com/cvxgrp/cvxstatarb)
