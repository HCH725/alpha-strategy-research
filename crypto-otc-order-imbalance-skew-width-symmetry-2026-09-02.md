---
schema: strategy-research-record-v1
title: "Exact Symmetry Reduction and First-Order Skew Translation in Over-The-Counter Order Imbalance Quoting"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - otc-trading
  - rfq
  - order-imbalance
  - quote-skewing
  - bid-ask-spread
  - inventory-risk
  - indifference-pricing
status: research-only
confidence: high
source_as_of: 2026-08-11
sources:
  - "Peter Cotton, 'On a Simple Relationship Between Order Imbalance, Skew and Width in Over-The-Counter Trading', arXiv:2608.07690v1 [q-fin.TR], August 11, 2026. DOI: 10.48550/arXiv.2608.07690. https://arxiv.org/abs/2608.07690"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Exact Symmetry Reduction and First-Order Skew Translation in Over-The-Counter Order Imbalance Quoting

## Provenance

- **Primary Source:** Peter Cotton (Intech Investments / Microprediction), *"On a Simple Relationship Between Order Imbalance, Skew and Width in Over-The-Counter Trading"*, arXiv preprint `arXiv:2608.07690v1 [q-fin.TR]`, submitted August 11, 2026. Full text: [https://arxiv.org/html/2608.07690v1](https://arxiv.org/html/2608.07690v1).
- **Primary Categories:** Trading and Market Microstructure (`q-fin.TR`), Mathematical Finance (`q-fin.MF`), Statistical Finance (`q-fin.ST`). MSC Codes: 91G15, 93E20.
- **Empirical Venue / Reference Context:** Theoretical and structural market-making model applicable to dealer-to-client request-for-quote (RFQ) and sealed-bid trading platforms (such as corporate bonds, municipal debt, crypto OTC desks, Paradigm/Enso RFQ protocols, and electronic FX dealer networks).

## Economic mechanism

### Source-reported

In over-the-counter (OTC) and request-for-quote (RFQ) environments, intermediaries acquire and dispose of inventory by responding to sequential sealed-bid customer enquiries against competing dealers. When customer flow exhibits directional imbalance—where the probability $q \in (0,1)$ of a seller enquiry differs from a buyer enquiry ($1-q$)—dealers adjust their quoting quotes.

Standard quantitative market-making literature (e.g., Avellaneda and Stoikov, 2008; Guéant et al., 2012) primarily focuses on inventory-driven skewing under symmetric arrival intensities ($q = 1/2$), typically producing constant-width linear-skew (CWLS) heuristics where quote skew is strictly driven by current signed inventory $x$.

Cotton (2026) proves that stationary market making under order imbalance ($q \neq 1/2$) exactly reduces to the balanced problem ($q = 1/2$) through an algebraic symmetry (birth-death symmetrization). Specifically, assuming best competing responses have a local hazard rate $h = 1/w$ (where $w$ is the observable market width), the imbalanced problem with carrying cost $c(x)$ maps exactly to a balanced problem with cost of carry inflated by $M(q)$, subject to three explicit closed-form adjustments:
1. **Midpoint Skew Translation:** The market maker translates their quoting midpoint by $\delta = \frac{w}{2} \ln\left(\frac{q}{1-q}\right)$.
2. **Non-Discretionary Spread Widening:** The non-discretionary quoting spread widens by $\gamma = \frac{1}{h} \ln\left(\frac{1}{2\sqrt{q(1-q)}}\right) \ge 0$.
3. **Cost-of-Carry Inflation:** The effective cost of holding inventory is multiplied by $M(q) = \frac{1}{2\sqrt{q(1-q)}} = e^{h\gamma} \ge 1$.

Key analytical theorems established by the author:
- **Zero-Inventory Skew (Corollary 1):** A dealer with zero inventory ($x=0$) still shades their quote by $\delta = \frac{w}{2} \ln\left(\frac{q}{1-q}\right)$. Flow shading is a first-order flow phenomenon, not an inventory artifact.
- **First-Order Skew vs Second-Order Width (Corollary 2):** Expanding about $q = 1/2$, the skew response is first-order linear in imbalance: $\delta \approx 2w\left(q - \frac{1}{2}\right) + \frac{8w}{3}\left(q - \frac{1}{2}\right)^3$, whereas the width response is second-order quadratic: $\gamma \approx 2w\left(q - \frac{1}{2}\right)^2 + 4w\left(q - \frac{1}{2}\right)^4$. This explains why practitioners instinctively skew quotes before widening spreads.
- **Inventory Cost Reveal:** The slope of indifference cost $\nu(x)$ determines skew, while its convexity determines discretionary width: $C(x) = \frac{\nu(x+s) - 2\nu(x) + \nu(x-s)}{2s}$. Quoting behavior directly reveals the dealer's underlying inventory cost function.
- **Recovery of CWLS:** The Constant Width Linear Skew heuristic is mathematically optimal only in the unique special corner of balanced flow ($q=1/2$) and a hyperbolic cosine cost of carry $c(x) \propto \cosh(2hC_0 x / s) - 1$.

### Research interpretation

This paper delivers an exact parameter-free bridge between observable flow imbalance $q$ and optimal automated quoting. Rather than executing expensive re-solves of dynamic programming or HJB equations whenever market order flow tilts:
1. **Decoupled Quoting Engine:** An OTC / RFQ market-making bot solves the balanced inventory equation once offline (or numerically for an arbitrary carry cost $c(x)$), then applies the three-parameter transformation $(\delta, \gamma, M(q))$ dynamically in real time using only rolling tape estimates of $q$ and local width $w$.
2. **Structural Skill Diagnostic:** The paper establishes that under exponential competitive hazard, optimal quoting yields a constant fill ratio $e^{-1} \approx 36.79\%$ on zero marginal inventory/adverse selection. Departures from this benchmark provide an explicit decomposition of trader quoting skill into flow-reading ($\delta$) vs inventory control ($S_\delta$).

## Signal

### 1. State Variables and Input Estimation
At enquiry arrival time $t$:
- $w_t$: Locally observed market width (reciprocal hazard rate of winning quotes, estimated from recent winning margin distribution).
- $q_t \in (0, 1)$: Probability that the incoming enquiry is a seller (customer selling / dealer buying), estimated from rolling window or EWMA of request directions.
- $x_t$: Current signed inventory of the market maker.
- $s$: Standard enquiry trade lot size.
- $\epsilon$: Expected adverse selection per won trade.
- $c(x)$: Underlying unit holding cost function ($c(0)=0$).

### 2. Symmetry Shift Parameters
Compute the three explicit transformations:
$$\delta(q_t, w_t) = \frac{w_t}{2} \ln \left(\frac{q_t}{1 - q_t}\right)$$
$$\gamma(q_t, w_t) = w_t \ln \left(\frac{1}{2\sqrt{q_t(1 - q_t)}}\right)$$
$$M(q_t) = \frac{1}{2\sqrt{q_t(1 - q_t)}} = \exp\left(\frac{\gamma(q_t, w_t)}{w_t}\right)$$

### 3. Indifference Valuation and Quoting Strikes
Let $\nu(x; M(q)c)$ be the steady-state indifference liquidation cost satisfying the balanced consistency equation:
$$\frac{s}{w_t} M(q_t) c(x) = \exp\left(-1 - \frac{\epsilon}{w_t}\right) \left[ \frac{1}{2} \exp\left(-\frac{\nu(x+s) - \nu(x)}{w_t}\right) + \frac{1}{2} \exp\left(-\frac{\nu(x-s) - \nu(x)}{w_t}\right) - \exp\left(-\frac{\nu(s) - \nu(0)}{w_t}\right) \right]$$

Define the discrete inventory cost differences:
$$S_\delta(x) = \frac{\nu(x+s) - \nu(x-s)}{2s} \quad (\text{balanced skew})$$
$$C(x) = \frac{\nu(x+s) - 2\nu(x) + \nu(x-s)}{2s} \quad (\text{discretionary half-width})$$

### 4. Quoting Rules
- **Bid Markdown (for incoming sell enquiry):**
  $$m^\downarrow(x) = w_t + \epsilon + \nu(x+s) - \nu(x) - \delta(q_t, w_t) + \gamma(q_t, w_t) = w_t + \gamma + \epsilon + s\left(S_\delta(x) + C(x)\right) - \delta$$
  $$\text{Bid Price} = P_{\text{fair}} - m^\downarrow(x)$$

- **Ask Markup (for incoming buy enquiry):**
  $$m^\uparrow(x) = w_t + \epsilon + \nu(x) - \nu(x-s) + \delta(q_t, w_t) + \gamma(q_t, w_t) = w_t + \gamma + \epsilon - s\left(S_\delta(x) - C(x)\right) + \delta$$
  $$\text{Ask Price} = P_{\text{fair}} + m^\uparrow(x)$$

- **Midpoint Quote Displacement:**
  $$\text{Mid Quote} = P_{\text{fair}} + \frac{m^\uparrow(x) - m^\downarrow(x)}{2} = P_{\text{fair}} + \delta(q_t, w_t) - s S_\delta(x)$$

## Required data

- **Venue / Protocol:** RFQ systems, dealer-to-dealer platforms, automated market maker (AMM) private market-maker hooks, or off-exchange crypto OTC venues (e.g., Paradigm, Wintermute OTC, Enso, Binance RFQ).
- **Timeframe / Event Cadence:** Event-driven at each RFQ arrival / quote refresh.
- **Fields:**
  - `enquiry_timestamp`: Timestamp of client enquiry.
  - `direction`: Direction indicator (1 for customer selling, 0 for customer buying).
  - `fair_price`: Benchmark reference mid-price (from liquid CEX spot/perp index).
  - `winning_quote` & `quote_responses`: Competitor quotes to calibrate local hazard parameter $w_t$.
  - `fill_status`: Binary trade fill / won indicator.
  - `inventory`: Current open inventory in units.
- **Point-in-Time Considerations:** Quote must be constructed within low-latency budget (<50ms) upon receipt of RFQ.

## Execution assumptions

- **Order Type:** Sealed-bid two-sided or single-sided RFQ quote response.
- **Fill Probability:** Log-linear win curve $P(\text{fill} \mid m) = \exp(-m/w_t)$ under local exponential competitor pricing.
- **Adverse Selection ($\epsilon$):** Modeled as fixed per-trade loss to informed toxic takers.
- **Inventory Carrying Cost ($c(x)$):** Modeled as borrowing fee, margin interest, or quadratic inventory variance penalty.

## Evidence

### Source-reported

- **Local Hazard Robustness:** Numerical verification in accompanying code (`verify_local_exponentiality.py`) demonstrates that the error in zero-inventory skew $\delta$ is approximately one-quarter of the hazard's relative variation across visited strike ranges, shrinking linearly with local constancy.
- **Analytical Optimality of CWLS:** Proof that CWLS requires holding cost $c(x) \propto \cosh(2hC_0 x / s) - 1$, which has relative error $(h S_\delta(x))^2 / 12$ compared to a pure quadratic cost.
- **Fill Ratio Invariant:** Proves that an optimal market maker facing zero adverse selection and flat marginal inventory cost achieves an exact win rate of $e^{-1} \approx 36.79\%$.
- **Empirical Literature Alignment:** Cites empirical RFQ findings in European corporate bonds (Fermanian et al., 2017) and electronic FX dealer internalizers (Butz and Oomen, 2019) showing persistent quote skewing on order flow at zero inventory.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- Theoretical limitation: If competitor quote distributions exhibit heavy polynomial tails or discrete clustered ladders rather than local exponential survival, the exact closed-form symmetry requires numerical correction.

## Falsification plan

1. **Zero-Inventory Skew Test:** Measure quote midpoints submitted by top liquidity providers at zero signed inventory across varying rolling 1-hour customer order imbalances $q \in [0.1, 0.9]$.
   - *Falsification Condition:* If observed quote skew fails to scale linearly with $\ln(q / (1-q))$ or deviates significantly from $\frac{w}{2} \ln(q / (1-q))$ in competitive RFQ venues, the exact exponential symmetry reduction is refuted.
2. **First-Order Skew vs Second-Order Width Scaling:** Regress empirical quote skew and quote width on $(q - 1/2)$ and $(q - 1/2)^2$.
   - *Falsification Condition:* If quote width exhibits a statistically significant first-order linear coefficient with $(q - 1/2)$, the prediction that width response is purely second-order is falsified.
3. **Carry Multiplier P&L Stress Test:** Backtest the transformed policy $(\delta, \gamma, M(q))$ against full dynamic programming under extreme flow skew ($q > 0.85$).
   - *Falsification Condition:* If the symmetry-reduced policy suffers $>5\%$ drawdown relative to exact DP numerical solution, the single-solve invariant fails under regime-shifting flow.

## Crypto portability

- **Interpretation:** Direct for Crypto OTC / RFQ; Adapted for Central Limit Order Book (CLOB) and AMM market making.
- **Application Contexts:**
  - *Institutional Crypto OTC / RFQ (Paradigm, Wintermute, Cumberland):* Direct 1-to-1 mapping. Customer request flow is heavily imbalanced during market selloffs or funding squeezes.
  - *Perpetual CLOB Market Making:* Asymmetric taker trade arrivals ($q$) shift the optimal reservation quote midpoint by $\delta = \frac{w}{2} \ln \frac{q}{1-q}$ before accumulating position inventory, reducing toxic adverse selection.
  - *MEV / Private Order Flow Auctions:* MEV searchers pricing private transactions can apply the exact cost multiplier $M(q)$ when quoting toxic vs non-toxic flow pools.
- **Crypto-Specific Frictions:** Extreme volatility spikes can violate local exponential hazard; 24/7 funding rate accrual must be added directly into the carrying cost function $c(x)$.

## Limitations

- **Stationary Imbalance Assumption:** Assumes $q$ is locally constant over the decision horizon; does not model Hawkes-driven self-exciting clustering of arrivals (addressed in companion work).
- **Homogeneous Trade Size:** Assumes all RFQs arrive with unit lot size $s$; real-world requests exhibit variable sizes requiring size-dependent strike discretization.
- **Local Exponentiality Dependency:** If competitor responses have multi-modal or fat-tailed distribution, the approximation error increases with inventory excursion depth.

## Implementation status

- `not-implemented`: Research capture only. No production implementation has been executed or verified in the research repository.

## Adoption boundary

- Research-only. Not approved for implementation, paper trading, testnet, or live deployment.

## Related Wiki records

- `[[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]]`
- `[[quant/crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01]]`
- `[[quant/microstructure-mean-reversion-optimal-symmetric-band-waiting-option-2026-09-02]]`

## Sources

- Peter Cotton, *"On a Simple Relationship Between Order Imbalance, Skew and Width in Over-The-Counter Trading"*, arXiv preprint `arXiv:2608.07690v1 [q-fin.TR]`, August 11, 2026. DOI: `10.48550/arXiv.2608.07690`. URL: [https://arxiv.org/abs/2608.07690](https://arxiv.org/abs/2608.07690).
- Marco Avellaneda and Sasha Stoikov, *"High-frequency trading in a limit order book"*, Quantitative Finance 8(3), 217–224, 2008.
- Olivier Guéant, Charles-Albert Lehalle, and Joaquin Fernandez-Tapia, *"Dealing with the inventory risk: a solution to the market making problem"*, Mathematics and Financial Economics 7(4), 477–507, 2012.
