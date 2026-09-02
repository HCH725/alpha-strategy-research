---
schema: strategy-research-record-v1
title: "Forecast-to-Fill: Benchmark-Neutral Trend-Momentum Alpha and Billion-Dollar Capacity in Gold Futures"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - trend-following
  - momentum
  - gold-futures
  - cme
  - market-microstructure
  - kelly-criterion
  - market-impact
  - volatility-targeting
status: research-only
confidence: high
source_as_of: 2026-09-02
sources:
  - "Mainak Singha, Jose Aguilera-Toste, and Vinayak Lahiri, 'Forecast-to-Fill: Benchmark-Neutral Alpha and Billion-Dollar Capacity in Gold Futures (2015-2025)', arXiv:2511.08571v1 [q-fin.TR], November 2025. DOI: 10.48550/arXiv.2511.08571. https://arxiv.org/abs/2511.08571"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Forecast-to-Fill: Benchmark-Neutral Trend-Momentum Alpha and Billion-Dollar Capacity in Gold Futures

## Provenance

- **Primary Source:** Mainak Singha (NASA / Catholic University of America), Jose Aguilera-Toste (MIT / Polytechnic University of Madrid), and Vinayak Lahiri (Panthéon-Sorbonne University), *"Forecast-to-Fill: Benchmark-Neutral Alpha and Billion-Dollar Capacity in Gold Futures (2015-2025)"*, arXiv preprint `arXiv:2511.08571v1 [q-fin.TR]`, November 2025. DOI: [10.48550/arXiv.2511.08571](https://doi.org/10.48550/arXiv.2511.08571). Stable URL: [https://arxiv.org/abs/2511.08571](https://arxiv.org/abs/2511.08571). Full HTML text: [https://arxiv.org/html/2511.08571v1](https://arxiv.org/html/2511.08571v1).
- **Subject Areas:** Trading and Market Microstructure (`q-fin.TR`), Computational Finance (`q-fin.CP`), Portfolio Management (`q-fin.PM`), Risk Management (`q-fin.RM`), Statistical Finance (`q-fin.ST`).
- **Research Setting:** The study examines the conversion of modest, state-dependent predictability in CME Gold futures into allocator-grade, market-neutral alpha through end-to-end "forecast-to-fill" engineering. The methodology integrates exponential smoothing slope extraction, momentum confirmation, EWMA volatility targeting, ATR-based stops, and a closed-form friction-adjusted Kelly criterion incorporating both linear costs and square-root temporary market impact.

## Economic mechanism

### Source-reported

The authors argue that systematic trading performance collapses between paper backtests and live trading because traditional modeling over-emphasizes predictive forecasting while treating execution, sizing, risk targeting, and market impact as secondary overlays.

In liquid commodity futures such as gold, institutional hedgers (miners, refiners, central banks, and ETF issuers) adjust large physical and derivative inventory positions slowly over daily-to-weekly horizons in response to macro, interest rate, and dollar shocks. Because these participants prioritize immediacy over timing, their order flow exerts persistent directional pressure on prices. The "Forecast-to-Fill" framework posits that short-horizon alpha represents a state-dependent risk premium: systematic trend-followers act as liquidity and inventory providers to institutional hedgers during sustained adjustment regimes, earning a compensation premium for holding directional exposure while hedgers pay a premium for immediacy.

### Research interpretation

The core falsifiable thesis is that **coupling an interpretable trend-momentum regime probability with volatility targeting and a friction-adjusted Kelly sizing function yields benchmark-neutral alpha ($\beta \approx 0.03$) and an asymmetric payoff profile (bounded downside, open-ended upside) in CME Gold futures, scalable up to approximately $1 billion AUM before market impact renders net growth non-positive**:

1. **Information Smoothing & Drift Extraction:** Daily prices exhibit high noise-to-signal ratios. Exponential moving average smoothing on log prices ($\tilde{y}_t$) extracts low-frequency drift, while standardization relative to a rolling 10-year window creates a stationary trend intensity $z$-score.
2. **Dual-Confirmation Regime Filter:** A continuous slope confidence score ($p_{\text{trend}}$) is blended with a 50-day discrete momentum filter ($I_{\text{mom}}$). Slope provides continuous regime intensity ("how strong"), while momentum ensures macro directional alignment ("which direction"), suppressing whipsaws in range-bound chop.
3. **Friction-Adjusted Kelly Sizing with Square-Root Impact:** Standard Kelly sizing ($f^\star = \mu / \sigma^2$) leads to severe over-allocation and rapid performance degradation under market impact. Incorporating a linear cost drag ($n k f$) and an Almgren-Chriss/Gatheral square-root impact penalty ($\gamma (n f)^{3/2}$) into log-utility growth produces a closed-form quadratic equation with an optimal participation bound that preserves positive compounding.
4. **Volatility Budgeting and Confidence Gating:** Sizing inversely to EWMA volatility forecasts standardizes risk across volatility regimes, while linear confidence shaping reduces exposure to zero during unconfirmed regimes ($p_{\text{bull}} \le 0.50$).
5. **Asymmetric Risk Management:** A combination of $2 \times \text{ATR}_{14}$ hard stops, $1.5 \times \text{ATR}_{14}$ trailing stops, a 30-day holding timeout, and regime-flip de-risking enforces a right-skewed return distribution with small left tails.

*Ported Hypothesis Note:* This mechanism was developed and evaluated exclusively on CME Gold futures. Any port to cryptocurrency assets is an adapted, unproven research hypothesis rather than crypto empirical evidence.

## Signal

The signal and sizing pipeline is deterministically specified from first principles:

### 1. Drift Extraction and Slope Standardization
Let $P_t > 0$ denote the settlement price of CME Gold futures on day $t$. Log-prices are $y_t = \log P_t$.
- **Exponential Smoothing:**
  $$\tilde{y}_t = \lambda \tilde{y}_{t-1} + (1 - \lambda) y_t, \quad \lambda \in (0, 1)$$
- **Smoothed Slope:**
  $$\Delta \tilde{y}_t = \tilde{y}_t - \tilde{y}_{t-1}$$
- **Standardization:**
  $$z_t = \frac{\Delta \tilde{y}_t - \mu_{\text{train}}}{\sigma_{\text{train}}}$$
  where $\mu_{\text{train}}$ and $\sigma_{\text{train}}$ are the sample mean and standard deviation of $\Delta \tilde{y}_t$ computed exclusively across the preceding 10-year training window.

### 2. Regime Probability Mapping
- **Trend Confidence:** Extreme values of $z_t$ are clipped to $[-3, 3]$ and affinely transformed to $[0, 1]$:
  $$p_{\text{trend}}(t) = \frac{\text{clip}(z_t, -3, 3) + 3}{6}$$
- **Momentum Direction Check ($K = 50$ days):**
  $$I_{\text{mom}}(t) = \mathbf{1}_{\{P_t > P_{t-50}\}}$$
- **Blended Regime Probability:**
  $$p_{\text{bull}}(t) = \omega p_{\text{trend}}(t) + (1 - \omega) I_{\text{mom}}(t), \quad p_{\text{bear}}(t) = 1 - p_{\text{bull}}(t)$$
  where $\omega = 0.60$ is calibrated on the training window and frozen out-of-sample.

### 3. Trade Activation and Direction
A long position is eligible if and only if the regime probability confirms bullish drift and the local slope is positive:
$$\text{Signal}_t = \mathbf{1}_{\{p_{\text{bull}}(t) \ge 0.52 \ \land \ \Delta \tilde{y}_t > 0\}}$$
*(The benchmark study evaluates long-only trades to reflect gold's asymmetric drift and physical carry characteristics; symmetric shorting is structurally possible but was omitted).*

### 4. Volatility Targeting & Confidence Shaping
- **EWMA Volatility Forecast:** Next-day variance is updated recursively forward:
  $$\hat{\sigma}_{t+1}^2 = \theta \hat{\sigma}_t^2 + (1 - \theta) r_t^2, \quad r_t = \frac{P_t}{P_{t-1}} - 1$$
  with memory decay $\theta$ estimated from the training window.
- **Target Daily Volatility:** Annual target $\sigma_{\text{ann}}^\star = 15\%$, converted to daily via $D = 252$:
  $$\sigma^\star = \frac{15\%}{\sqrt{252}} \approx 0.9449\%$$
- **Volatility-Targeted Weight Cap:**
  $$w_t^{(\text{vol})} = \min\left(W_{\max}, \frac{\sigma^\star}{\hat{\sigma}_{t+1}}\right), \quad W_{\max} = 2.0$$
- **Confidence Shaping:**
  $$s_t = \max\left(0, 2(p_{\text{bull}}(t) - 0.5)\right) \in [0, 1]$$
  $$w_t^{(\text{target})} = s_t \cdot w_t^{(\text{vol})}$$

### 5. Friction-Adjusted Kelly Position Sizing
Under linear transaction cost $k = 0.7$ bps and square-root impact parameter $\gamma = 0.02$ for $n = 1$ round-trip per day, expected daily log-growth as a function of leverage fraction $f$ is:
$$g(f) \approx \mu f - \frac{1}{2}\sigma^2 f^2 - n k f - \gamma (n f)^{3/2}$$
Setting $x \equiv \sqrt{f}$, differentiating $g(x)$, and setting to zero yields the quadratic equation:
$$2\sigma^2 x^2 + 3\gamma n^{3/2} x - 2(\mu - n k) = 0$$
The unique positive root defining the optimal fraction is:
$$x^\star = \frac{-3\gamma n^{3/2} + \sqrt{9\gamma^2 n^3 + 16\sigma^2(\mu - n k)}}{4\sigma^2}, \quad f^\star = (x^\star)^2$$
(if $\mu - n k \le 0$, $f^\star = 0$).
- **Fractional Kelly Multiplier:** $\tilde{f} = \lambda_{\text{Kelly}} f^\star$ with $\lambda_{\text{Kelly}} = 0.40$.
- **Baseline Allocation:** If $\tilde{f} \approx 0$, a minimum baseline exposure of $0.25 \times w_t^{(\text{vol})}$ is maintained to avoid artificial zeroing in uncertain but positive states.
- **Executable Portfolio Weight:**
  $$w_t = \text{Signal}_t \cdot \min\left(w_t^{(\text{target})}, \tilde{f} \cdot w_t^{(\text{vol})}\right)$$

### 6. Exit Rules
Once active, an open position exits under the earliest of:
1. **Hard Stop:** Price falls below entry by $> 2 \times \text{ATR}_{14}(t)$.
2. **Trailing Stop:** Price drops by $> 1.5 \times \text{ATR}_{14}(t)$ from its running maximum peak.
3. **Timeout:** Position age reaches 30 trading days.
4. **Regime De-Risking:** If $p_{\text{bear}}(t) > 0.50$, the position is halved or closed immediately.

## Required data

- **Instrument:** CME Gold Futures (ticker `GC`), continuous front-month contract.
- **Roll Convention:** Rolled two business days prior to First Notice Date; returns include roll P&L.
- **Reference Regressor:** LBMA Gold Price PM Fix (used strictly as an exogenous benchmark regressor in CAPM tests, never in trade signal generation).
- **Timeframe:** Daily settlement prices (16:00 ET close).
- **Fields:** Daily Open, High, Low, Close (Settlement) prices, Volume, and Open Interest.
- **Point-in-Time Discipline:** All training-window parameters ($\lambda, \mu_{\text{train}}, \sigma_{\text{train}}, \omega, \theta, \mu, \sigma, \mu_u, \sigma_u, f^\star$) are estimated over a 10-year rolling window and frozen before the subsequent 6-month out-of-sample testing slice. Within the test slice, filtering is strictly recursive ($t$ uses only $\mathcal{F}_t$).
- **Timestamp Alignment:** Signal generated at day $t$ close $\mathcal{F}_t$; executed at $t+1$ close (baseline $T+1$ execution).
- **Missing Data / Holidays:** NYSE / CME holiday schedule; last known settlement price is carried forward (never the return).

## Execution assumptions

- **Execution Timing:** Baseline fill at $t+1$ close ($T+1$). Robustness checks evaluate $T+0$ and $T+2$.
- **Order Type:** Market-on-Close (MOC) or limit order executed at settlement.
- **Linear Transaction Costs:** $k = 0.7$ basis points (0.007%) per round-trip trade, covering exchange fees, clearing, broker commissions, and half-spread.
- **Market Impact Model:** Square-root temporary impact $\text{impact}_t \approx Y \sigma_{\text{1d}} \sqrt{q_t}$, where $q_t$ is participation rate relative to Average Daily Volume ($\text{ADV}_t$). Reduced-form daily growth impact penalty parameterized by $\gamma = 0.02$.
- **Leverage Limit:** Capped at $W_{\max} = 2.0$ (maximum 200% gross notional exposure).
- **Turnover & Rebalance Frequency:** Maximum 1 round-trip per day ($n \le 1$); mean absolute portfolio weight $|w_t| \approx 0.0326$; mean active-day turnover $|\Delta w_t| \approx 0.066$.

## Evidence

### Source-reported

All empirical metrics below are directly quoted from Singha, Aguilera-Toste, and Lahiri (arXiv:2511.08571v1, November 2025):

- **Sample Period:** January 2015 to October 31, 2025 (2,793 out-of-sample trading days, ~11 years), rolling 10-year train $\to$ 6-month test walk-forward.
- **Headline FAST Configuration (Net of $0.7$ bps linear cost and $\gamma = 0.02$ impact):**
  - **Sharpe Ratio:** 2.88.
  - **Bootstrap 95% Confidence Interval:** $[2.49, 3.27]$ (1,000 stationary block bootstraps, block length = 20 days).
  - **Annualized Return:** 2.62% (at realized annualized volatility of 0.91%).
  - **Realized Annual Volatility:** 0.91% (low realized volatility is due to frequent zero-exposure and partial confidence gating).
  - **Compound Annual Growth Rate (CAGR):** 2.65% at 0.91% realized vol.
  - **Maximum Drawdown:** 0.52%.
  - **Calmar Ratio:** 5.11.
  - **Win Rate / Hit Rate (Calendar Days):** 26.67%.
  - **Profitable Months:** 79.1% up-months.
  - **Trading Activity:** 1,282 entries; 1,132 active exposure days ($|w_t| > 10^{-3}$, representing 40.5% of the sample).
  - **Active-Day Statistics:**
    - Active-day hit rate: 65.8%.
    - Average gain: +6.00 bps.
    - Average loss: -4.01 bps.
    - Payoff ratio: 1.49x.
    - Expected value per active day: +2.58 bps.
    - Annualized active-day expectancy: $2.58 \text{ bps} \times (1,132 / 2,793) \times 252 \approx 2.63\%$ (reconciling with realized CAGR of 2.65%).
- **Benchmark Neutrality (CAPM Regression vs. Spot Gold):**
  - Annualized $\alpha$: 2.25% ($t = 9.53, p < 0.001$).
  - $\beta$ to Spot Gold: 0.03 ($t = 31.01$).
  - $R^2$: 0.001 (explaining less than 0.1% of strategy variance).
  - Volatility-Matched Information Ratio (IR): 2.09.
- **15% Volatility Target Scaling:**
  - Implied Annualized Return: 43.2% per year.
  - Implied Benchmark-Neutral Alpha: 37.1% per year (IR-based $\alpha = \text{IR} \times \text{TE} \approx 37\%$; linear regression $\alpha \approx 43\%$).
  - Sharpe (2.88) and IR (2.09) remain invariant under linear scaling.
- **Capacity Frontier:**
  - Growth curve: $g(L) = \mu_u L - \frac{1}{2}(\sigma_u L)^2 - n k L - \gamma (n L)^{3/2}$.
  - Estimated parameters: $\mu_u = 1.0 \times 10^{-4}$, $\sigma_u = 5.7 \times 10^{-4}$, $k = 0.7$ bps, $\gamma = 0.02, n = 1$.
  - Zero-growth point: $L_{\text{zero}} \approx 0.0033$.
  - At CME gold ADV of $\sim \$50$ billion/day, capacity frontier supports approximately **$0.8 to $1.0 billion AUM** ($\sim 0.07\%$ ADV participation).
- **Sub-Period Stability:**
  - Sharpe ratios persist near 2.9 across rolling multi-year slices (2015–2017, 2018–2020, 2021–2023, 2024–2025).
  - Sub-period drawdowns never exceed 0.60%.
- **Regime Attribution:**
  - Bull regime ($p_{\text{bull}} > 0.55$): Sharpe 3.82, annualized return 4.49%.
  - Chop regime ($0.45 \le p_{\text{bull}} \le 0.55$): Sharpe ~0.0, return flat.
  - Bear regime ($p_{\text{bull}} < 0.45$): Strategy remains inactive, return flat.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Cost Sensitivity:** When linear cost $k$ and square-root impact $\gamma$ are doubled ($2.0\times$ baseline, i.e., $k = 1.4$ bps, $\gamma = 0.04$), net Sharpe ratio deteriorates close to 0.0, indicating that alpha is strictly bounded by high execution costs.
- **Signal Inversion (Placebo Test):** Reversing the trade signal (shorting on bullish triggers) yields a Sharpe ratio of -2.95, demonstrating that the edge is entirely directional and sensitive to correct trend specification.
- **Component Ablation:** Removing the trend slope extraction collapses Sharpe; removing the momentum confirmation indicator creates substantial whipsaw losses in choppy regimes. Both components are non-linearly complementary.
- **Latency Decay:** Moving from immediate execution ($T+0$) to $T+1$ and $T+2$ delays reduces Sharpe from 2.88 to 2.25. While positive, the edge decays with operational latency.
- **Single-Asset Constraint:** The empirical results are established exclusively on CME Gold futures. Testing on broader commodity or currency markets was not performed in the paper.
- **None identified in the reviewed sources for negative findings on the mathematical derivation of the friction-adjusted Kelly fraction; absence is not evidence of no negative result.**

## Falsification plan

To falsify or disconfirm the "Forecast-to-Fill" mechanism, the following operational tests are specified:

1. **Transaction Cost Multiplier Stress:** Re-run the walk-forward backtest increasing round-trip slippage and fees to 2.5 bps, 5.0 bps, and 10.0 bps. **Failure Rule:** If net Sharpe ratio drops below 1.0 at $\le 3.0$ bps round-trip cost, the strategy lacks execution robustness.
2. **Order Execution Delay (Latency Stress):** Simulate fills executed at $T+3$ and $T+5$ settlement closes. **Failure Rule:** If Sharpe ratio drops below 0.5 at $T+3$, the strategy relies on short-lived transient information rather than durable multi-day institutional drift.
3. **Shuffled / Placebo Returns Test:** Randomly shuffle daily log return increments while preserving sample volatility and run the exact pipeline. **Failure Rule:** If the synthetic series produces a Sharpe ratio $\ge 1.0$, the observed historical performance is an artifact of curve-fitting.
4. **Superior Predictive Ability (SPA) Benchmark Test:** Evaluate against a universe of 500+ random technical indicators using Hansen's SPA test. **Failure Rule:** If the SPA $p$-value exceeds 0.05, the performance difference is not statistically distinguishable from data mining.
5. **Alternative Volatility Target Stress:** Rebalance targeting 5%, 10%, 20%, and 25% annualized volatility. **Failure Rule:** If maximum drawdown scales non-linearly with target volatility (e.g., MaxDD $> 15\%$ at 15% vol), the risk-targeting and ATR stop mechanisms fail risk parity.
6. **Cross-Asset Portability Failure:** Apply identical parameters to Brent Crude (`CL`), Euro FX (`6E`), and 10-Year Treasuries (`ZN`). **Failure Rule:** If all three assets produce negative net Sharpe after 1.0 bps costs, the mechanism is an overfitted gold anomaly rather than a general macro inventory-risk premium.

## Crypto portability

**adapted / unproven**

The mechanism originates from traditional commodity futures (CME Gold) and must be treated as an **adapted and unproven research hypothesis** when ported to cryptocurrency markets. The cited paper provides zero empirical validation in crypto assets.

Key crypto portability challenges and structural differences:
- **24/7 Trading vs. Discrete Fixes:** Gold futures feature a distinct daily settlement fix (16:00 ET) and weekend closures. Crypto perpetuals trade 24/7/365 without formal session closes, requiring arbitrary UTC snapshot boundaries (e.g., 00:00 UTC) which may introduce boundary sensitivity.
- **Perpetual Funding Rate Drag:** In crypto perpetual futures (BTCUSDT, ETHUSDT), holding long positions during sustained bullish regimes incurs 8-hour funding rate payments. In extreme bull regimes, funding rates annualized at 20–80% could fully consume the 2.62% unleveraged drift or significantly degrade the 37% scaled alpha.
- **Exchange Fragmentation and Liquidity Depth:** CME Gold futures concentrate global institutional liquidity ($~\$50$ billion ADV) into a central limit order book with minimal counterparty risk. Crypto perpetual liquidity is fragmented across Binance, OKX, Bybit, and Hyperliquid. Market impact parameters ($\gamma$) for large orders are substantially higher, lowering the practical AUM capacity threshold from $1 billion to $< \$50 million.
- **Volatility Scaling:** Crypto annualized volatility regularly exceeds 50–80%, compared to gold's 12–18%. A 15% volatility target would require significant de-leveraging (average position weights $< 0.20$), amplifying the impact of fixed exchange fees.

## Limitations

- **Single-Asset Scope:** Tested exclusively on CME Gold futures; generalizability across other commodity sectors (energy, agriculture, metals) or digital assets is unproven.
- **Unleveraged Return vs. Volatility-Scaled Alpha:** The headline unleveraged return is 2.62% per year at 0.91% realized volatility. The cited 43% return and 37% alpha require scaling exposure to a 15% annual volatility budget, assuming continuous linear scalability and friction stability.
- **Static Impact Parameterization:** The square-root impact parameter ($\gamma = 0.02$) and linear friction ($k = 0.7$ bps) are held constant rather than dynamically estimated from instantaneous order book depth.
- **Long-Only Asymmetry:** The study does not evaluate short-side trading, assuming long-only drift due to gold's monetary inflation-hedge role.
- **Model Simplifications:** Volatility forecasting relies on a 20-day EWMA rather than high-frequency realized volatility (HAR-RV) or GARCH models.
- **Not independently reproduced in internal backtesting stack.**

## Implementation status

No implementation in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader). The record documents theoretical and empirical findings from the external literature only.

## Adoption boundary

This record is research material only. Its presence in this repository does **not** constitute strategy adoption, approval for implementation, or authorization for Paper, Testnet, or Live trading. All quantitative figures represent source-reported results from arXiv:2511.08571v1 and have not been validated on internal execution infrastructure.

## Related Wiki records

- [[futures-trend-following-autocorrelation-drift-decomposition-2026-09-02]] — Explores continuous-time autocorrelation and drift decomposition across 84 futures contracts (arXiv:2607.19497v1); provides the macroeconomic and statistical foundation for why trend-following persistence exists.
- [[futures-volatility-normalized-tick-size-trend-following-filter-2026-09-02]] — Analyzes microstructural tick-size constraints and transaction-cost decay in futures trend-following (arXiv:2607.01550v1); directly complementary to the friction-adjusted Kelly sizing derivation.
- [[kellyboost-growth-optimal-gbdt-portfolio-construction-2026-09-02]] — Formulates Kelly-optimal growth under tree-based portfolio construction; shares the log-utility growth optimization objective.
- [[commodity-futures-hierarchical-graph-learning-calendar-spread-2026-09-02]] — Focuses on cross-commodity and term-structure spread dynamics, contrasting with single-asset directional forecast-to-fill execution.

## Sources

1. Singha, M., Aguilera-Toste, J., & Lahiri, V. (2025). "Forecast-to-Fill: Benchmark-Neutral Alpha and Billion-Dollar Capacity in Gold Futures (2015-2025)." *arXiv preprint arXiv:2511.08571v1 [q-fin.TR]*. DOI: [10.48550/arXiv.2511.08571](https://doi.org/10.48550/arXiv.2511.08571). URL: [https://arxiv.org/abs/2511.08571](https://arxiv.org/abs/2511.08571).
2. Almgren, R., & Chriss, N. (2001). "Optimal execution of portfolio transactions." *Journal of Risk*, 3(2), 5–40.
3. Gatheral, J. (2010). "No-dynamic-arbitrage and market impact." *Quantitative Finance*, 10(7), 749–759.
4. Hansen, P. R. (2005). "A test for superior predictive ability." *Journal of Business & Economic Statistics*, 23(4), 365–380.
