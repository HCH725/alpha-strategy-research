---
schema: strategy-research-record-v1
title: "Physical Crash Frontier under Finite Option Quotes: Second-Order Cone Programming Bounding of Crash Probabilities and Expected Tail Loss"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - options
  - risk-management
  - crash-probability
  - second-order-cone-programming
  - pricing-kernel
  - tail-risk
  - physical-measure
status: research-only
confidence: high
source_as_of: 2026-08-24
sources:
  - "Jirong Zhuang, 'The Physical Crash Frontier: What Finite Option Quotes Can and Cannot Reveal', arXiv:2608.23274v1 [q-fin.MF, q-fin.RM, q-fin.PR], August 24, 2026. DOI: 10.48550/arXiv.2608.23274. https://arxiv.org/abs/2608.23274"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Physical Crash Frontier under Finite Option Quotes: Second-Order Cone Programming Bounding of Crash Probabilities and Expected Tail Loss

## Provenance

- **Primary Source:** Jirong Zhuang (School of Operations Research and Information Engineering, Cornell University), *"The Physical Crash Frontier: What Finite Option Quotes Can and Cannot Reveal"*, arXiv preprint `arXiv:2608.23274v1 [q-fin.MF, q-fin.RM, q-fin.PR]`, submitted August 24, 2026. DOI: [10.48550/arXiv.2608.23274](https://doi.org/10.48550/arXiv.2608.23274). Full text: [https://arxiv.org/abs/2608.23274](https://arxiv.org/abs/2608.23274).
- **Primary Categories:** Mathematical Finance (`q-fin.MF`), Risk Management (`q-fin.RM`), Probability (`math.PR`), Computational Finance (`q-fin.CP`).
- **Context:** Addresses the fundamental quantitative problem of extracting physical (real-world $\mathbb{P}$) crash probability $\mathbb{P}(S_T \le K_{\mathrm{crash}})$ and conditional expected loss from observable cross-sectional option market prices. Because risk-neutral $\mathbb{Q}$-probabilities reflect both physical risk and variance risk premia (overstating physical crash probability), risk managers adjust via a stochastic pricing kernel. However, because real markets quote only a finite set of discrete strikes with non-zero bid-ask spreads, an infinite family of physical distributions fits market quotes. Zhuang constructs the exact non-parametric "physical crash frontier" via finite Second-Order Cone Programming (SOCP).

## Economic mechanism

### Source-reported

In options markets:
1. **The Risk-Neutral / Physical Divergence:** Out-of-the-money (OTM) put options trade at significant implied volatility premia due to investor risk aversion and downside hedging demand. Estimating physical tail risk directly from risk-neutral density $\mathbb{Q}$ severely exaggerates crash likelihood.
2. **Pricing Kernel Transformation:** Under a standard power-utility pricing kernel $m(R) = \frac{1}{R_f} \frac{R^{-\gamma}}{\mathbb{E}^{\mathbb{P}}[R^{-\gamma}]}$ with relative risk aversion $\gamma > 0$, physical expectations relate to risk-neutral option prices through moment ratios:
   $$\mathbb{P}(R \le \kappa) = \frac{\mathbb{E}^{\mathbb{Q}}[\mathbf{1}_{\{R \le \kappa\}} R^\gamma]}{\mathbb{E}^{\mathbb{Q}}[R^\gamma]}$$
3. **The Finite-Quote Spread Constraint:** Market observations provide only discrete interval constraints $C_i^{\mathrm{bid}} \le \mathbb{E}^{\mathbb{Q}}[(R - k_i)^+] \le C_i^{\mathrm{ask}}$ and $P_j^{\mathrm{bid}} \le \mathbb{E}^{\mathbb{Q}}[(k_j - R)^+] \le P_j^{\mathrm{ask}}$. The set of admissible physical distributions forms a compact convex set in the plane of $(\text{Crash Probability } p, \text{Expected Tail Loss } \ell)$.
4. **Second-Order Cone Duality:** Computing the exact boundary (support function) of the attainable physical crash set reduces to solving finite Second-Order Cone Programs (SOCP). Zhuang proves that incorporating all available market quotes across the strike spectrum shrinks the admissible crash probability interval by a median of $\sim 80\%$ compared to classical two-strike put bounds (such as Breeden-Litzenberger or simple sandwich bounds).
5. **The Tail-Dilution Pathology:** Zhuang demonstrates an important theoretical impossibility result: finite option quotes alone cannot establish a positive lower bound (floor) for physical crash probability without an explicit external upper-tail restriction on returns, because unbounded mass in the far right tail inflates the denominator moment $\mathbb{E}^{\mathbb{Q}}[R^\gamma]$, driving the lower crash bound toward zero.

### Research interpretation

The falsifiable thesis is that **SOCP-derived physical crash bounds provide a superior predictive filter for tail-risk hedging and volatility risk premium (VRP) selling compared to raw risk-neutral variance metrics (VIX / DVOL)**:
- Options sellers entering short volatility positions based solely on elevated VIX/implied volatility suffer catastrophic losses during true structural tail events because risk-neutral indicators conflate crash risk with pure variance premium.
- Conditioning short-volatility / put-writing exposure on the SOCP upper physical crash bound $\bar{p}_{\mathrm{crash}}$ allows the strategy to harvest VRP during high-premium/low-physical-risk regimes while hedging or deleveraging when the admissible physical crash set shifts sharply upward.

## Signal

### 1. Cross-Sectional Option Quote Ingestion

At time $t$:
- Collect underlying spot price $S_t$, forward price $F_t,T$, risk-free rate $r$, and expiration horizon $T - t$.
- Ingest full strike grid $\{K_i\}_{i=1}^N$ with bid-ask pairs $(C_i^{\mathrm{bid}}, C_i^{\mathrm{ask}})$ for calls and $(P_j^{\mathrm{bid}}, P_j^{\mathrm{ask}})$ for puts.
- Specify normalized crash threshold return $\kappa_{\mathrm{crash}} = K_{\mathrm{crash}} / S_t$ (e.g., $-15\%$ or $-20\%$ drop).
- Calibrate or sweep risk aversion parameter $\gamma \in [1.0, 5.0]$ (baseline $\gamma = 2.5$).

### 2. SOCP Boundary Computation

For direction vector $\theta = (\cos \alpha, \sin \alpha) \in \mathbb{R}^2$, compute the support function $h(\theta)$ by solving the primal SOCP:
$$\max_{\mu \in \mathcal{M}_+} \theta_1 \int_0^{\kappa_{\mathrm{crash}}} R^\gamma d\mu(R) + \theta_2 \int_0^{\kappa_{\mathrm{crash}}} (\kappa_{\mathrm{crash}} - R) R^\gamma d\mu(R)$$
subject to:
$$\int_0^\infty R^\gamma d\mu(R) = 1$$
$$C_i^{\mathrm{bid}} \le \int_0^\infty (R - k_i)^+ d\mu(R) \le C_i^{\mathrm{ask}}, \quad \forall i$$
$$P_j^{\mathrm{bid}} \le \int_0^\infty (k_j - R)^+ d\mu(R) \le P_j^{\mathrm{ask}}, \quad \forall j$$
$$\int_0^{\bar{R}_{\max}} d\mu(R) = 1 \quad (\text{tail truncation regularization to prevent dilution})$$

### 3. Alpha / Risk Overlay Rule

- **Upper Bound Physical Crash Probability:** $\bar{p}_t = \max \mathbb{P}(S_T \le K_{\mathrm{crash}})$.
- **Lower Bound Physical Crash Probability:** $\underline{p}_t = \min \mathbb{P}(S_T \le K_{\mathrm{crash}})$.
- **Crash Uncertainty Width:** $\Delta p_t = \bar{p}_t - \underline{p}_t$.
- **Trading Decision Logic:**
  - **Regime A (VRP Harvest):** If Implied Volatility / Risk-Neutral Put Price is elevated ($z_{\mathrm{IV}} > 1.5$) BUT Upper Crash Probability $\bar{p}_t \le \tau_{\mathrm{safe}}$ (e.g., $\le 2.5\%$ for 1-month horizon), write delta-hedged OTM puts / short strangles (harvesting pure volatility risk premium).
  - **Regime B (Tail Risk Deleveraging / Crash Hedge):** If $\bar{p}_t > \tau_{\mathrm{crash}}$ (e.g., $> 8.0\%$) or crash uncertainty $\Delta p_t$ expands by $> 2\sigma$, close all short option positions and buy deep OTM puts as tail protection.

## Required data

- **Instruments:** SPX / SPY options on CBOE; BTC and ETH options on Deribit.
- **Option Chain Snapshots:**
  - End-of-day or 15-minute cross-sectional strike grids across expiries ($T \in [7\text{d}, 90\text{d}]$).
  - Firm bid and ask prices, open interest, and bid-ask spread filters.
- **Underlying Cash / Futures Price:** Synchronized spot index and perpetual / forward curves.

## Execution assumptions

- **Execution Timing:** Weekly or daily rebalancing at option market close (16:00 ET for US equities, 08:00 UTC for Deribit crypto options).
- **Transaction Costs:** Full bid-ask spread crossing on option executions plus exchange taker fees ($0.03\%$ on Deribit, $\$0.50$/contract on US equities).
- **Delta Hedging:** Delta-neutral underlying rebalancing executed daily via spot or perpetual futures.

## Evidence

### Source-reported

All empirical results, SOCP proofs, and bounding tightness statistics reported below are from Jirong Zhuang (arXiv:2608.23274v1, August 2026):
1. **Spread Tightening vs. Standard Bounds:**
   - On historical S&P 500 weekly option cross-sections (1996--2023), solving the full SOCP incorporating all quoted strikes reduces the width of the admissible crash probability interval by a median of **80.2%** compared to classical two-point put bounds.
2. **Identification of Tail Dilution:**
   - Proves mathematically that without an upper support bound $\bar{R}_{\max}$, the infimum physical crash probability is trivially 0 for any finite set of quotes, resolving a persistent contradiction in earlier literature that assumed non-zero lower bounds without identifying the implicit tail assumption.
3. **Out-of-Sample Crash Forecasting:**
   - The SOCP upper crash bound $\bar{p}_t$ correctly spiked prior to historical systemic market dislocations (including 2008 Lehman collapse, 2011 US debt downgrade, and March 2020 COVID shock), whereas risk-neutral variance indicators frequently produced false alarms during benign earnings spikes.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Illiquid Deep OTM Strikes:** In strikes with wide bid-ask spreads ($> 50\%$ of mid-price) or stale quotes, the SOCP feasible set expands significantly, degrading bounding precision unless strict liquidity filtering is applied.
- **Pricing Kernel Sensitivity:** Admissible bounds depend monotonically on assumed risk aversion $\gamma$; misspecification of $\gamma$ by $\pm 1.0$ shifts the upper crash probability by up to $\pm 1.8$ percentage points.

## Falsification plan

1. **Physical Crash Realization Test:** Track realized out-of-sample crash events ($S_T \le 0.85 S_t$ over 30-day horizons) against forecasted SOCP bounds $[\underline{p}_t, \bar{p}_t]$ across 10 years of option data. Falsification threshold: If empirical crash frequency exceeds the predicted upper bound $\bar{p}_t$ in $> 5\%$ of roll periods (at 95% confidence level), reject the SOCP pricing kernel bounding validity.
2. **VRP Strategy Alpha Overlay Test:** Compare a delta-hedged short-strangle strategy gated by $\bar{p}_t \le 2.5\%$ against an ungated short-strangle benchmark. Falsification threshold: If the SOCP-gated strategy does not reduce maximum drawdown by at least 40% while preserving $\ge 85\%$ of annualized return over a full 5-year cycle, reject the economic value of the crash frontier filter.
3. **Deribit Crypto Options Out-of-Sample Calibration:** Test the SOCP optimizer on Deribit BTC/ETH option chains during severe crypto liquidation cascades. Falsification threshold: If the SOCP optimization fails to find a feasible solution in $> 1.0\%$ of liquid option snapshots, reject numerical stability in crypto markets.

## Crypto portability

- **Adapted / Direct for Crypto Options**:
- Deribit provides a deep, liquid 24/7 options order book for BTC and ETH with rich strike granularity suitable for SOCP discretization.
- **Crypto-Specific Considerations:**
  - **Inverse Option Contract Specifications:** Deribit BTC and ETH options are coin-margined (inverse payout structure: payoffs settled in BTC/ETH rather than USD), requiring conversion of payoff equations into USD-numeraire before SOCP solver ingestion.
  - **Higher Tail Convexity:** Crypto option volatility smiles exhibit substantially steeper negative skew and higher implied kurtosis than equity indices, requiring wider strike grids ($K \in [0.2 S_0, 3.0 S_0]$) and explicit handling of heavy fat tails.

## Limitations

- **Not independently reproduced:** Theoretical and empirical results from Zhuang (arXiv:2608.23274v1, 2026).
- **Requires Convex Optimization Solver:** Computing real-time crash frontiers requires fast SOCP solvers (e.g., MOSEK, Clarabel, or SCS) integrated into the trading engine.
- **Risk Aversion Prior $\gamma$:** The framework requires an exogenous choice of pricing kernel curvature $\gamma$.

## Implementation status

- `not-implemented`
- Research capture only. No SOCP solver or options risk overlay implemented in PyBroker, Nautilus, or live options execution infrastructure.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not authorize live options trading, volatility selling, or options tail risk hedging.

## Related Wiki records

- `[[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]`
- `[[quant/crypto-options-volatility-risk-premium-zscore-2026-08-31]]`
- `[[quant/crypto-deribit-options-volatility-of-volatility-vov-realized-quarticity-2026-09-01]]`
- `[[quant/crypto-options-implied-correlation-dispersion-2026-08-31]]`

## Sources

1. Jirong Zhuang, *"The Physical Crash Frontier: What Finite Option Quotes Can and Cannot Reveal"*, arXiv preprint `arXiv:2608.23274v1 [q-fin.MF, q-fin.RM, q-fin.PR]`, submitted August 24, 2026. DOI: [10.48550/arXiv.2608.23274](https://doi.org/10.48550/arXiv.2608.23274). Stable URL: https://arxiv.org/abs/2608.23274.
