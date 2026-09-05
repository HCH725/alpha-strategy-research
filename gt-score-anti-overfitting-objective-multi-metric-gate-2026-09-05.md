---
schema: strategy-research-record-v1
title: "The GT-Score: Multi-Metric Gated Anti-Overfitting Objective Function for Algorithmic Strategy Optimization"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - objective-function
  - overfitting-mitigation
  - walk-forward-validation
  - statistical-significance
  - downside-deviation
  - equity-curve-linearity
  - equities
  - meta-strategy
status: research-only
confidence: high
source_as_of: 2026-01-08
sources:
  - "arXiv:2602.00080v1 [q-fin.ST], 1 February 2026. https://arxiv.org/abs/2602.00080"
  - "https://doi.org/10.3390/jrfm19010060"
  - "https://arxiv.org/html/2602.00080v1"
  - "Alexander Pearson Sheppert, 'The GT-Score: A Robust Objective Function for Reducing Overfitting in Data-Driven Trading Strategies', Journal of Risk and Financial Management (JRFM), 2026, 19(1), 60."
  - "https://github.com/shep-analytics/gt_score (commit c3cfefa800dd86d23743128ba14736c482abc2e1)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# The GT-Score: Multi-Metric Gated Anti-Overfitting Objective Function for Algorithmic Strategy Optimization

## Provenance

- **Primary Source:** Alexander Pearson Sheppert (University of the Cumberlands, Williamsburg, KY, USA), *"The GT-Score: A Robust Objective Function for Reducing Overfitting in Data-Driven Trading Strategies"*, published in *Journal of Risk and Financial Management (JRFM)*, 2026, 19(1), 60; preprint submitted to arXiv on February 1, 2026 as `arXiv:2602.00080v1 [q-fin.ST]`.
- **Canonical DOI:** [10.3390/jrfm19010060](https://doi.org/10.3390/jrfm19010060)
- **Canonical Web Abstract:** [https://arxiv.org/abs/2602.00080](https://arxiv.org/abs/2602.00080)
- **Canonical HTML Full Text:** [https://arxiv.org/html/2602.00080v1](https://arxiv.org/html/2602.00080v1)
- **Official Open-Source Implementation & Snapshot:**
  - GitHub Repository: [https://github.com/shep-analytics/gt_score](https://github.com/shep-analytics/gt_score)
  - Immutable Commit SHA: `c3cfefa800dd86d23743128ba14736c482abc2e1`
  - Core Modules: `src/gt_score.py`, `src/backtester.py`, `src/walkforward.py`, `src/loss_functions.py`, `src/optimizers.py`, `strategies/RSI_Strategy.py`, `strategies/BollingerBands_Strategy.py`, `strategies/MACD_Strategy.py`
  - Supplementary Processed Data: `output/results/monte_carlo_complete_summary.json`, `output/results/walkforward_complete_summary.json`, `output/results/statistical_tests.json`, `output/tables/table1_summary.tex`, `output/tables/table2_walkforward.tex`, `output/tables/table3_ablation.tex`, `output/tables/table4_sensitivity.tex`
- **Deduplication Audit:** A comprehensive audit of the `alpha-strategy-research` repository confirmed zero prior captures referencing `2602.00080`, `GT-Score`, `Sheppert`, `shep-analytics`, or `10.3390/jrfm19010060`.
  - While other optimization records exist in the repository (e.g., `finance-grounded-loss-functions-band-turnover-crypto-2026-09-05.md` investigating differentiable neural network loss functions like `LogMDD` and `ModSharpe` with turnover regularization on crypto perpetuals; `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` evaluating decision regret bounds in convex portfolio allocation; and `two-stage-adaptive-shrinkage-golden-criterion-equity-premium-2026-09-02.md`), the GT-Score is an independent, non-differentiable combinatorial meta-objective explicitly designed for black-box parameter optimization (random search, Bayesian optimization, genetic algorithms) across discrete trading rules.

## Economic mechanism

### Source-reported

In systematic trading and data-driven financial modeling, the standard quantitative pipeline searches over hundreds or thousands of parameter combinations and rule variants. Selecting the best in-sample backtest among many candidates represents a severe multiple-testing and data-snooping pitfall (White 2000; Sullivan, Timmermann & Granger 1999; Bailey et al. 2014; Harvey, Liu & Zhu 2016). When conventional loss functions such as total profit ($\mathcal{L}_{\text{simple}} = -\text{Profit}$), Sharpe ratio ($\mathcal{L}_{\text{Sharpe}} = -E[R]/\sigma$), or Sortino ratio ($\mathcal{L}_{\text{Sortino}} = -E[R]/\sigma_d$) are used as search objectives:
1. They aggressively exploit idiosyncrasies and noise clusters in historical training samples, leading to substantial performance decay out-of-sample (optimism bias).
2. They ignore whether outperformance relative to buy-and-hold exceeds standard sampling noise.
3. They permit parameter sets that generate lumpy, erratic equity curves dominated by a few outlier trades (low path consistency).

To counter this, Sheppert introduces the GT-Score (Golden Ticket Score), which embeds anti-overfitting regularizers directly into the optimization objective rather than attempting post-hoc deflations. The GT-Score is formulated as:
$$\text{GT-Score} = \frac{\mu \cdot \ln(z) \cdot R^2}{\sigma_d}$$
where:
- $\mu$: mean return per trade (or per observation period), rewarding profitability.
- $\ln(z)$: natural logarithm of the standardized excess return $Z$-score ($z = \frac{\mu - \mu_m}{\sigma / \sqrt{N}}$), which functions as a non-linear significance gate. It anchors at $z=1$ ($\ln(1) = 0$), smoothly penalizes marginally positive or noisy returns ($0 < z \le 1$), heavily penalizes underperformance ($z \le 0$), and logarithmically dampens extreme $z$-scores to prevent high-frequency noise exploitation.
- $R^2$: coefficient of determination from linear regression of cumulative trade percentage returns over trade sequence, enforcing smooth, consistent capital compounding and penalizing outlier-driven windfalls.
- $\sigma_d$: downside deviation (standard deviation of negative returns), penalizing drawdown risk while leaving upside volatility unpenalized.
- $n_{\min} = 50$: trade frequency floor enforcing a minimal statistical sampling base.

### Research interpretation

The GT-Score acts as a composite multi-gate filter in parameter space:
- **Significance Gate ($\ln(z)$):** Parameter sets that generate returns barely exceeding buy-and-hold are rejected before they enter out-of-sample testing. By penalizing $z \le 1$, the optimizer avoids the zero-alpha noise regime.
- **Path Smoothness Regularizer ($R^2$):** Many technical indicators produce high total return due to 1 or 2 macro trend spikes while suffering long bleeding periods. Demanding a high $R^2$ on trade-by-trade cumulative returns forces the parameter search toward invariant, steady edge rather than regime-dependent flukes.
- **Asymmetric Risk Adjustment ($\sigma_d$):** Traditional Sharpe penalizes upside outliers identically to downside crashes. Replacing $\sigma$ with $\sigma_d$ ensures that strategies capturing strong right-tail momentum are not penalized.

Component Decomposition:
- **Core Signal Engine:** Any underlying parameterized rule set (e.g., RSI overbought/oversold, Bollinger Band width/lookback, MACD moving average combinations).
- **Optimization Gate:** GT-Score composite objective with piecewise penalty functions for $z \le 0$ and $0 < z \le 1$.
- **Sample Stability Filter:** Minimum trade count constraint $n_{\min} = 50$ (or optional variance-stabilization periodization).

## Signal

The GT-Score is an objective function that evaluates and ranks parameterized trading strategies during model selection. The complete operational implementation is structured as follows:

### Mathematical Formulation & Piecewise Gating

Given a backtest evaluation containing $N$ completed trades with trade returns $r_i$ ($i = 1, \dots, N$):
1. **Mean Strategy Return ($\mu$):**
   $$\mu = \frac{1}{N} \sum_{i=1}^N r_i$$
2. **Mean Benchmark Return ($\mu_m$):**
   $$\mu_m = \left(\frac{P_{\text{end}}}{P_{\text{start}}}\right)^{1/N} - 1$$
   where $P_{\text{start}}$ and $P_{\text{end}}$ are the asset closing prices at the start and end of the backtest window (`source-reported benchmark definition for trade mode`).
3. **Return Standard Deviation ($\sigma$):**
   $$\sigma = \sqrt{\frac{1}{N} \sum_{i=1}^N (r_i - \mu)^2}$$
4. **Standardized Excess Z-Score ($z$):**
   $$z = \frac{\mu - \mu_m}{\sigma / \sqrt{N}}$$
5. **Equity Curve Smoothness ($R^2$):**
   Computed as the squared Pearson correlation coefficient $r^2$ from linear regression of cumulative percentage returns $C_k = \sum_{j=1}^k r_j$ against trade index $k \in \{1, \dots, N\}$.
6. **Downside Deviation ($\sigma_d$):**
   $$\sigma_d = \sqrt{\frac{1}{N_d} \sum_{r_i < 0} r_i^2}$$
   with numerical smoothing parameter $\epsilon = 10^{-6}$ applied if no negative returns occur ($N_d = 0$).

### Piecewise Objective Calculation (Source-reported minimization score)

- **Trade Threshold Penalty ($N \le n_{\min} = 50$):**
  $$\text{Score} = 999 - \left(N \cdot \frac{999 - 100}{50}\right)$$
  ensuring any parameterization producing $\le 50$ trades is strictly dominated by acceptable candidates.
- **Case 1: Underperformance ($z \le 0$):**
  $$\text{Score} = 100 + 100 \cdot \left(1 - \exp(-|z - 1|)\right)$$
  yielding a heavy penalty $> 100$ that grows monotonically as underperformance worsens.
- **Case 2: Marginal Outperformance ($0 < z \le 1$):**
  $$\text{Score} = 100 \cdot \left(1 - \exp(-|z - 1|)\right)$$
  producing a smooth transition penalty between $0.0$ and $63.2$.
- **Case 3: Statistically Significant Outperformance ($z > 1$):**
  $$\text{Score} = -\frac{\mu \cdot \ln(z) \cdot R^2}{\sigma_d}$$
  (negated to convert maximization into a standard minimization objective).

### Evaluated Underlying Trading Strategies (Source-reported)

1. **Relative Strength Index (RSI) Momentum Reversal:**
   - Lookback window: $w \in [5, 30]$ days.
   - Long entry: RSI crosses below oversold threshold $\theta_{\text{buy}} \in [10, 40]$ from above:
     $$\text{RSI}_t < \theta_{\text{buy}} \quad \text{and} \quad \text{RSI}_{t-1} \ge \theta_{\text{buy}}$$
   - Long exit: RSI crosses above overbought threshold $\theta_{\text{sell}} \in [60, 90]$:
     $$\text{RSI}_t > \theta_{\text{sell}} \quad \text{and} \quad \text{RSI}_{t-1} \le \theta_{\text{sell}}$$
2. **Bollinger Bands Mean Reversion:**
   - Lookback window: $w \in [10, 50]$ days; standard deviation multiplier $k \in [1.0, 3.0]$.
   - Long entry: Close price crosses below lower band $\mu_w - k \cdot \sigma_w$:
     $$\text{Close}_t < \text{LowerBand}_t \quad \text{and} \quad \text{Close}_{t-1} \ge \text{LowerBand}_{t-1}$$
   - Long exit: Close price crosses above upper band $\mu_w + k \cdot \sigma_w$:
     $$\text{Close}_t > \text{UpperBand}_t \quad \text{and} \quad \text{Close}_{t-1} \le \text{UpperBand}_{t-1}$$
3. **MACD Trend Following:**
   - Fast EMA span: $s_f \in [8, 16]$; Slow EMA span: $s_s \in [20, 32]$; Signal span: $s_{\text{sig}} \in [5, 12]$.
   - Long entry: MACD line crosses above Signal line:
     $$\text{MACD}_t > \text{Signal}_t \quad \text{and} \quad \text{MACD}_{t-1} \le \text{Signal}_{t-1}$$
   - Long exit: MACD line crosses below Signal line (or optional TP/SL trigger).

### Operational Execution Conventions

- **Signal formation timestamp:** Daily close ($t$) after market close calculation (`source-reported daily OHLCV bar processing`).
- **Order timing:** Next-day open / execution at daily close with optional spread/commission modeling (`source-reported simulation convention`).
- **Position sizing:** 100% of portfolio equity allocated to asset upon buy signal, full cash exit upon sell signal (`source-reported backtesting engine logic`).
- **Evaluation budget:** 25 random search evaluations per asset/seed split (`source-reported budget`).

## Required data

- **Instrument / Universe:** Top 50 companies of the S&P 500 by market capitalization (`source-reported equity universe`).
- **Data Vendor & Ingestion:** Yahoo Finance API (`yfinance`) historical daily data (`source-reported data source`).
- **Historical Period:** January 1, 2010 through December 31, 2024 (~3,770 trading days per asset) covering recovery, low-rate bull market, 2020 COVID shock, and 2022 rate hike cycles (`source-reported sample`).
- **Required Fields:** Daily Open, High, Low, Close, Volume (OHLCV).
- **Point-in-Time & Embargo:**
  - 4-year rolling training window.
  - 2-year forward validation window.
  - 1-year forward roll step.
  - 30-day strict embargo period between training window end and validation window start to prevent autocorrelation leakage (`source-reported walk-forward specification`).

## Execution assumptions

- **Fill Model:** Daily event-driven simulation. Buy order filled at $\text{Close} + \text{spread}$; sell order filled at $\text{Close} - \text{spread}$ (`source-reported execution mechanism`).
- **Slippage & Spread:** Default spread = $\$0.0001$ per share (`source-reported default`); sensitivity analysis tested per-side cost across $[0, 10]$ basis points (`source-reported in Section 5.1`).
- **Commission:** Default commission rate = $0.0001$ ($0.01\%$) of trade value (`source-reported backtester default`).
- **Shorting / Borrow:** Long-only equity execution; capital held in cash during flat periods (`source-reported portfolio model`).
- **Capital & Leverage:** Initial cash = $\$1,000,000$, zero leverage ($1.0\times$ maximum gross exposure) (`source-reported starting balance`).

## Evidence

### Source-reported

All quantitative performance figures, statistical tests, and ablation findings below are traced directly to Sheppert (JRFM 2026 / arXiv:2602.00080v1) and the verified snapshot files in `output/results/`:

1. **Walk-Forward Validation (9 Sequential Splits, 2014–2024, 5,340 Trials across 50 Stocks):**
   - **Generalization Ratio ($\text{Return}_{\text{val}} / \text{Return}_{\text{train}}$):**
     - **GT-Score:** **$0.3655$** (Validation Return: $18.52\% \pm 37.08\%$, Training Return: $50.67\% \pm 62.70\%$).
     - **Sharpe Loss:** $0.1796$ (Validation Return: $17.10\% \pm 34.11\%$, Training Return: $95.21\% \pm 114.79\%$).
     - **Sortino Loss:** $0.1860$ (Validation Return: $18.57\% \pm 35.03\%$, Training Return: $99.86\% \pm 115.58\%$).
     - **Simple Profit Loss:** $0.1879$ (Validation Return: $18.96\% \pm 35.43\%$, Training Return: $100.91\% \pm 115.95\%$).
   - **Overfitting Reduction:** GT-Score improved the generalization ratio by **$+98.1\%$** relative to baseline objective functions ($0.3655$ vs. $0.1845$ baseline average), indicating that GT-Score selected parameterizations retained nearly twice as much of their training performance on unseen data.
   - **Validation Return Comparison:** Out-of-sample validation returns between GT-Score and baselines showed no statistically significant deficit:
     - vs. Sharpe: mean difference $+1.42\%$, $t$-statistic $= 1.028$, $p = 0.3041$ (not statistically different).
     - vs. Sortino: mean difference $-0.05\%$, $t$-statistic $= -0.038$, $p = 0.9696$.
     - vs. Simple: mean difference $-0.44\%$, $t$-statistic $= -0.320$, $p = 0.7491$.

2. **Monte Carlo Robustness Study (9,000 Optimization Trials, 15 Random Seeds 42–56):**
   - **Out-of-Sample Performance:**
     - **GT-Score:** Mean test return = **$43.55\%$** ($\text{std} = 62.55\%$, median = $27.11\%$, IQR = $[5.01\%, 67.41\%]$), mean training return = $237.77\%$, overfitting ratio = **$0.1832$**, mean trades = $32.4$.
     - **Sharpe:** Mean test return = $46.31\%$ ($\text{std} = 71.72\%$, median = $28.83\%$), mean training return = $395.61\%$, overfitting ratio = $0.1170$, mean trades = $21.2$.
     - **Sortino:** Mean test return = $49.34\%$ ($\text{std} = 76.15\%$, median = $30.38\%$), mean training return = $421.35\%$, overfitting ratio = $0.1171$, mean trades = $20.6$.
     - **Simple:** Mean test return = $49.52\%$ ($\text{std} = 76.21\%$, median = $31.24\%$), mean training return = $428.00\%$, overfitting ratio = $0.1157$, mean trades = $21.1$.
   - **Generalization Ratio Advantage:** GT-Score demonstrated a $+56.5\%$ higher retention of training performance ($0.1832$ vs. $\sim 0.117$).
   - **Paired Statistical Tests (2,250 Paired Trials vs. GT-Score):**
     - **vs. Sharpe:** Mean difference $= -2.75\%$ (95% CI: $[-4.98\%, -0.61\%]$), paired $t = -2.452$, $p = 0.0143$ ($*$), Cohen's $d = -0.041$ (negligible/small effect). Wilcoxon signed-rank $p = 0.1387$ (non-significant non-parametrically).
     - **vs. Sortino:** Mean difference $= -5.79\%$ (95% CI: $[-8.09\%, -3.62\%]$), paired $t = -5.051$, $p = 4.74 \times 10^{-7}$ ($***$), Cohen's $d = -0.083$ (small effect). Wilcoxon $p = 2.88 \times 10^{-5}$ ($***$).
     - **vs. Simple:** Mean difference $= -5.97\%$ (95% CI: $[-8.30\%, -3.81\%]$), paired $t = -5.217$, $p = 1.99 \times 10^{-7}$ ($***$), Cohen's $d = -0.086$ (small effect). Wilcoxon $p = 1.27 \times 10^{-5}$ ($***$).
   - The trade-off is clear: while conventional objectives achieve slightly higher raw in-sample and out-of-sample returns by aggressively overfitting, GT-Score curbs extreme in-sample variance, resulting in significantly more dependable out-of-sample behavior.

3. **Ablation Study (Table 3 in Supplementary Results):**
   Evaluating the marginal contribution of each term to out-of-sample validation return:
   - **Full GT-Score:** Mean validation return = **$0.150$** ($\text{std} = 0.065$).
   - **Ablating $\ln(z)$:** Mean return drops to $0.082$ ($\text{std} = 0.095$, $\Delta = -0.068$).
   - **Ablating $R^2$:** Mean return drops to $0.098$ ($\text{std} = 0.088$, $\Delta = -0.052$).
   - **Ablating $\sigma_d$:** Mean return drops to $0.062$ ($\text{std} = 0.105$, $\Delta = -0.088$).
   - All three components are necessary; removing downside deviation ($\sigma_d$) causes the largest single degradation, followed closely by the significance gate ($\ln(z)$).

4. **Transaction Cost Sensitivity Analysis (Section 5.1):**
   - GT-Score strategies execute slightly higher trade counts ($32.4$ vs. $\sim 21.0$ trades per test window).
   - Evaluating frictional costs across $0$ to $10$ bps per side confirmed that while raw net returns decay monotonically, the relative ranking of objective functions is robust to moderate execution friction.

### Independently reproduced

Not independently reproduced in internal quantitative backtesting frameworks (PyBroker/Nautilus). Independent source verification was performed directly on the primary manuscript text and the cloned GitHub repository `https://github.com/shep-analytics/gt_score` at commit `c3cfefa800dd86d23743128ba14736c482abc2e1`.

### Negative evidence

- **Slight Raw Return Discount:** GT-Score deliberately sacrifices $2.7\%$ to $5.9\%$ of raw out-of-sample return compared to unconstrained profit or Sortino maximization. If an institutional mandate prioritizes unconstrained capital accumulation over equity curve stability, GT-Score may appear conservative.
- **Sensitivity to High Friction / Turnover:** Because GT-Score favors consistent, smaller gains across more trades (mean $32.4$ vs. $21.0$), in high-fee retail environments (e.g., $10\text{--}20$ bps taker fees on spot crypto or wide bid-ask spreads in illiquid equities), the higher trade frequency could diminish net outperformance.
- **Parametric Gaussian Assumption in $Z$-Score:** The $z$-score gate $\sigma / \sqrt{N}$ assumes independent, approximately Gaussian error distributions. Financial returns exhibit excess kurtosis and conditional heteroskedasticity (Cont 2001), which can overstate the effective sample size $N$ during periods of heavy autocorrelation.

## Falsification plan

To falsify the claim that GT-Score systematically outperforms conventional objective functions (Sharpe, Sortino, Simple) in out-of-sample generalization and stability, execute the following pre-declared empirical tests:

1. **Out-of-Sample Generalization Parity Test:**
   - *Protocol:* Evaluate GT-Score versus Sharpe and Sortino across a distinct equity universe (e.g., Russell 2000 small caps or S&P MidCap 400) using identical 4-year train / 2-year validation splits with 30-day embargoes.
   - *Falsification Condition:* If GT-Score's generalization ratio fails to exceed the average baseline generalization ratio by at least $25\%$ (`research-defined falsification threshold`), the hypothesis of superior generalization transfer is falsified.
2. **Heavy-Tail Stress & Autocorrelation Disconfirmation Test:**
   - *Protocol:* Inject synthetic or observed autoregressive, fat-tailed noise (Student's $t$ with degrees of freedom $\nu \in [2.5, 4.0]$) into trade return series to test whether the parametric $z$-score gate degrades into false-positive selections.
   - *Falsification Condition:* If replacing $z = (\mu - \mu_m)/(\sigma/\sqrt{N})$ with a stationary block-bootstrap $p$-value gate reduces strategy turnover and improves out-of-sample Sharpe by $> 0.30$ (`research-defined falsification threshold`), the parametric Gaussian formulation is deemed inadequate.
3. **Execution Fee and Turnover Attrition Gate:**
   - *Protocol:* Backtest GT-Score-selected parameters under varying round-trip friction levels ($5, 10, 20, 30$ bps).
   - *Falsification Condition:* If the net out-of-sample return of GT-Score drops below that of Sortino/Sharpe at fee levels $\le 10$ bps round-trip (`research-defined falsification threshold`), GT-Score's turnover bias is identified as an implementation failure.
4. **Permutation / Placebo Label Shuffling Test:**
   - *Protocol:* Randomly permute the order of returns before computing $R^2$. If the optimization surfaces identical parameter sets with permuted sequence ordering, the $R^2$ path-consistency term is non-binding.

## Crypto portability

- **Portability Status:** `adapted` / `unproven`.
- **Traditional Asset Origin:** The primary empirical evaluation was conducted exclusively on 50 large-cap U.S. equities using daily OHLCV bars from 2010 to 2024. The paper contains zero cryptocurrency backtests or digital asset data.
- **Adaptation Challenges & Crypto Realities:**
  1. **Benchmark Definition ($\mu_m$):** In equity research, buy-and-hold of the single underlying stock is natural ($\mu_m = (P_{\text{end}}/P_{\text{start}})^{1/N} - 1$). In crypto perpetuals or multi-token baskets, holding cash or delta-neutral funding arbitrage is common. For crypto market-neutral or directional strategies, $\mu_m$ must be explicitly defined as either BTC buy-and-hold, an equal-weighted basket benchmark, or zero (`research-proposed benchmark convention`).
  2. **24/7 Session Structure:** Equities feature clear daily closes and overnight gaps. Crypto operates continuously; trade periodization must be pegged to UTC midnight (00:00 UTC) or fixed hourly intervals rather than exchange trading halts (`research-proposed operational adaptation`).
  3. **High Fee Sensitivity:** Crypto exchanges impose maker/taker fee tiers ($1\text{--}5$ bps for VIP/institutional, up to $5\text{--}7.5$ bps for retail). Because GT-Score rewards trade count consistency ($n \ge 50$), applying GT-Score without strict fee modeling could lead to unprofitable churning.
  4. **Funding Rates in Perpetuals:** For perpetual contracts, holding positions across 8-hour funding timestamps introduces variable holding costs that must be deducted from trade returns $r_i$ before calculating $\mu$ and $\sigma_d$.
  5. **Extreme Kurtosis:** Crypto assets exhibit fat tails far exceeding large-cap equities (kurtosis often $> 15$). The Gaussian $Z$-score denominator ($\sigma/\sqrt{N}$) will substantially overstate statistical confidence unless degrees-of-freedom adjustments or bootstrap standard errors are integrated.

## Limitations

- **Parametric Gaussian Significance Filter:** The $z$-score gate assumes independent, identically distributed normal returns. Realized trading returns exhibit skewness, fat tails, and clustering, which can distort the significance threshold.
- **Absence of Microstructure & Execution Modeling:** The primary study relies on daily close-to-close or open-to-open fills with nominal fixed spreads ($\$0.0001$). Intraday market impact, order book depth, liquidity constraints, and fill slippage were not modeled.
- **Equity-Only Universe:** Validated only on top 50 S&P 500 equities; performance on low-liquidity small caps, commodities, FX, or crypto remains unproven.
- **Long-Only Binary Allocation:** The reference backtester allocates $100\%$ equity to open positions and $0\%$ to closed positions; continuous position sizing and portfolio-level risk parity were omitted.
- **Computational Overhead in Large Searches:** Calculating $R^2$ via linear regression and $Z$-scores across thousands of parameter trials adds minor CPU overhead compared to simple cumulative sum metrics.

## Implementation status

- `not-implemented`: This research capture documents an external peer-reviewed study and public code release. No production code, PyBroker strategy, NautilusTrader actor, or live trading script has been implemented in this repository or associated execution engines.
- Research capture does not authorize deployment or verify operational edge in live market environments.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- **Boundary Conditions:** Inclusion in this repository does **not** constitute an approved trading strategy, validation of alpha edge, or authorization for live or paper capital allocation. Any potential integration into NautilusTrader or PyBroker requires an independent implementation proposal, rigorous historical attrition testing, transaction cost verification, and formal review.

## Related Wiki records

- `finance-grounded-loss-functions-band-turnover-crypto-2026-09-05.md` (Khubiyev et al. 2026, differentiable loss functions including `LogMDD`, `ModSharpe`, and `TvrReg` on crypto assets).
- `smart-predict-then-optimize-spo-plus-robust-portfolio-2026-09-05.md` (Wang & Hasuike 2026, decision regret bounds for portfolio optimization).
- `crypto-walk-forward-window-optimization-double-oos-momentum-2026-09-04.md` (Walk-forward parameterization and double out-of-sample validation on digital assets).
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]` (Canonical validation standards, purging, and embargo mechanics).

## Sources

- **Primary Article:** Alexander Pearson Sheppert, *"The GT-Score: A Robust Objective Function for Reducing Overfitting in Data-Driven Trading Strategies"*, *Journal of Risk and Financial Management*, 2026, 19(1), 60. DOI: [10.3390/jrfm19010060](https://doi.org/10.3390/jrfm19010060).
- **arXiv Preprint:** arXiv:2602.00080v1 [q-fin.ST], 1 February 2026. URL: [https://arxiv.org/abs/2602.00080](https://arxiv.org/abs/2602.00080).
- **arXiv Full Text HTML:** [https://arxiv.org/html/2602.00080v1](https://arxiv.org/html/2602.00080v1).
- **Official Open-Source Repository:** `shep-analytics/gt_score` on GitHub. URL: [https://github.com/shep-analytics/gt_score](https://github.com/shep-analytics/gt_score). Verified immutable commit SHA: `c3cfefa800dd86d23743128ba14736c482abc2e1`.
- **Public Data Source:** Yahoo Finance API via `yfinance` Python library ([https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/)).
