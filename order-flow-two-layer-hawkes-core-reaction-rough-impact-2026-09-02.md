---
schema: strategy-research-record-v1
title: "Two-Layer Hawkes Order Flow: Core-Reaction Decomposition, Fractional Hurst Memory, and Rough Market Impact Equilibrium"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - order-flow
  - market-microstructure
  - hawkes-processes
  - rough-volatility
  - market-impact
  - square-root-law
  - high-frequency-trading
status: research-only
confidence: high
source_as_of: 2026-01-30
sources:
  - "Johannes Muhle-Karbe, Youssef Ouazzani Chahdi, Mathieu Rosenbaum, Grégoire Szymanski, 'A Unified Theory of Order Flow, Market Impact, and Volatility', arXiv:2601.23172v1 [q-fin.TR, q-fin.ST], January 30, 2026. DOI: 10.48550/arXiv.2601.23172. https://arxiv.org/abs/2601.23172"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Two-Layer Hawkes Order Flow: Core-Reaction Decomposition, Fractional Hurst Memory, and Rough Market Impact Equilibrium

## Provenance

- **Primary Source:** Johannes Muhle-Karbe (Imperial College London), Youssef Ouazzani Chahdi (École Polytechnique), Mathieu Rosenbaum (École Polytechnique), and Grégoire Szymanski (Imperial College London), *"A Unified Theory of Order Flow, Market Impact, and Volatility"*, arXiv preprint `arXiv:2601.23172v1 [q-fin.TR, q-fin.ST]`, submitted January 30, 2026, revised February 2, 2026. DOI: [10.48550/arXiv.2601.23172](https://doi.org/10.48550/arXiv.2601.23172). Full text: [https://arxiv.org/abs/2601.23172](https://arxiv.org/abs/2601.23172).
- **Primary Categories:** Quantitative Finance - Trading and Market Microstructure (`q-fin.TR`), Statistical Finance (`q-fin.ST`).
- **Context:** A foundational microscopic limit order book (LOB) model proving that a single fundamental statistic—the core order flow persistence parameter $H_0 \approx 3/4$—simultaneously governs and unifies persistent signed order flow, rough volatility, rough volume, and the concave square-root law of market impact under no-arbitrage constraints.

## Economic mechanism

### Source-reported

Empirical financial economics exhibits three well-established macroscopic scaling regularities that have historically been modeled independently:
1. **Persistent Signed Order Flow:** Order signs exhibit power-law auto-correlations decaying slowly with lag $\tau^{-\gamma}$ ($\gamma \approx 0.5$, indicating long memory).
2. **Rough Volatility and Volume:** Realized log-volatility behaves as a rough fractional Brownian motion with Hurst parameter $H \in (0, 1/2)$, typically close to 0.1, and trading volume displays similar roughness ($H_{\text{vol}} \approx 0.25$).
3. **Square-Root Law of Market Impact:** The expected price impact of executing a metaorder of size $Q$ scales concavely as $I(Q) \sim Y \sigma \sqrt{Q / V}$.

Muhle-Karbe, Ouazzani Chahdi, Rosenbaum, and Szymanski (2026) introduce a two-layer Hawkes branching architecture:
- **Layer 1: Core Orders ($N^c$):** Represents exogenous institutional metaorder execution (fundamental trades split over time), displaying persistent self-excitation with Hurst parameter $H_0$.
- **Layer 2: Reaction Flow ($N^r$):** Represents endogenous high-frequency responses by liquidity providers, algorithmic market makers, and statistical arbitrageurs responding to order book imbalances.

The authors prove that under microscopic no-arbitrage (martingale price condition at macroscopic scales), the entire market ecosystem scales from $H_0$:
- Signed order flow converges to the sum of a fractional Brownian motion with Hurst index $H_0$ and a standard Brownian martingale.
- Realized volatility converges to a rough Heston / fractional Volterra process with Hurst parameter:
  $$H_{\text{vol}} = 2H_0 - \frac{3}{2}$$
- Traded volume magnitude scales with Hurst index:
  $$H_{\text{volume}} = H_0 - \frac{1}{2}$$
- The price impact function follows a power law with exponent:
  $$\alpha_{\text{impact}} = 2 - 2H_0$$
When calibrated to empirical microstructure data ($H_0 \approx 0.75$), the model analytically predicts:
- Rough volatility Hurst $H = 2(0.75) - 1.5 = 0$ (log-roughness);
- Rough volume Hurst $H_{\text{vol}} = 0.75 - 0.5 = 0.25$;
- Market impact exponent $\alpha = 2 - 2(0.75) = 0.50$, proving that the empirical square-root law ($I(Q) \propto Q^{0.5}$) is a direct mathematical consequence of core order persistence and market-making reaction balance.

### Research interpretation

The actionable alpha hypothesis from the two-layer Hawkes framework is a **structural dislocation filter between core institutional drift and transient reaction flow**:
1. At high frequencies (sub-second to 1-minute), order flow is dominated by the reaction layer $N^r$, which introduces temporary microstructural noise and transient inventory imbalances.
2. Filtering out the reaction Hawkes component isolates the latent core process $N^c$.
3. Directional price drift is driven entirely by the core metaorder process $N^c$, while deviations created by aggressive reaction flow represent transient liquidity overshoots that must mean-revert to the core trajectory to preserve no-arbitrage.

## Signal

### Two-Layer Hawkes Intensity Model
Total order arrivals are modeled as marked point processes $(N_t^{c,+}, N_t^{c,-}, N_t^{r,+}, N_t^{r,-})$ for buy/sell core and reaction orders:
$$\lambda_t^{c, \pm} = \mu_0^{c, \pm} + \int_0^t \phi_{cc}(t-s) dN_s^{c, \pm}$$
$$\lambda_t^{r, \pm} = \mu_0^{r, \pm} + \int_0^t \phi_{rc}(t-s) dN_s^{c, \pm} + \int_0^t \phi_{rr}(t-s) dN_s^{r, \mp}$$
where the core kernel $\phi_{cc}(t) \sim c_0 t^{-(1/2 + H_0)}$ generates the fractional persistence $H_0$.

### Core Order Estimator
1. **Calibration:** Estimate kernel parameters $(\mu_0, \phi_{cc}, \phi_{rc}, \phi_{rr})$ using maximum likelihood on tick-level trade and quote (TAQ) data over a rolling 20-day calibration window.
2. **State Estimation:** Compute the conditional core order imbalance:
   $$\text{COI}_t = \mathbb{E}\left[\lambda_t^{c, +} - \lambda_t^{c, -} \mid \mathcal{F}_t\right]$$
3. **Reaction Imbalance:** Compute the endogenous reaction flow imbalance:
   $$\text{ROI}_t = \lambda_t^{r, +} - \lambda_t^{r, -}$$
4. **Structural Dislocation Signal ($\Delta_t$):**
   $$\Delta_t = \text{COI}_t - \kappa \cdot \text{ROI}_t$$
   where $\kappa$ is the theoretical equilibrium coupling coefficient.

### Trading Logic
- **Long Signal:** $\Delta_t > \theta_{\text{entry}}$ (Core buying exceeds reaction absorption; entry price has not yet fully reflected institutional metaorder accumulation). Enter long.
- **Short Signal:** $\Delta_t < -\theta_{\text{entry}}$ (Core selling exceeds reaction absorption). Enter short.
- **Exit Signal:** $|\Delta_t| \le \theta_{\text{exit}}$ (Core flow dissipates and price impact fully catches up to fair value) OR time stop $T_{\text{max}} = 5 \text{ minutes}$.

## Required data

- **Instruments:** High-liquidity equities, index futures, or major cryptocurrency perpetuals (BTC-USDT, ETH-USDT).
- **Data Granularity:** Message-level Limit Order Book (L3) or tick-by-tick Trades and Quotes (TAQ) with microsecond timestamps, order book event types (insertions, cancellations, aggressive executions), and order sizes.
- **Fields:** Timestamp, EventType (Add, Cancel, Fill), Price, Size, Aggressor Side (Buy/Sell).
- **Point-in-time:** Online causal recursive filtering of Hawkes intensities without future look-ahead.

## Execution assumptions

- **Order Types:** Aggressive IOC limit orders placed at the top-of-book (best ask for buy, best bid for sell) or passive post-only orders when quoting the mean-reverting reaction leg.
- **Latency Budget:** Total round-trip execution latency $< 5 \text{ ms}$ for high-frequency crypto/equity venues.
- **Fee Model:** Maker/taker fee schedules (e.g., $-0.5\text{ bps}$ maker $/ +2.0\text{ bps}$ taker in crypto; equity per-share exchange rebates).
- **Market Impact:** Expected impact governed by the theoretical power-law $I(Q) \approx Y \sigma (Q/V)^{2 - 2H_0}$.

## Evidence

### Source-reported

- Muhle-Karbe, Ouazzani Chahdi, Rosenbaum, and Szymanski (2026, arXiv:2601.23172) establish rigorous mathematical proofs:
  1. Under macroscopic scaling limits, the two-layer Hawkes framework with heavy-tailed core memory parameter $H_0 \approx 0.75$ uniquely reconciles fractional order flow, rough volatility ($H \approx 0$), rough volume ($H_{\text{vol}} \approx 0.25$), and the square-root impact law ($\alpha = 0.5$).
  2. Proof that no-arbitrage in the scaling limit enforces a strict structural relationship between the reaction kernel and the core kernel, preventing statistical arbitrage across macroscopic horizons while creating well-defined microstructural price adjustment dynamics.
  3. Empirical estimation on institutional tick data validates the central $H_0 \approx 3/4$ scaling across multiple asset classes.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- High-frequency queue replenishment: in venues with high cancel-to-trade ratios (e.g., Binance, NASDAQ), high-frequency quote flickering can inject spurious jumps into reaction flow intensity estimation.
- In low-liquidity or fragmented crypto venues, core metaorders are frequently disguised across multiple venues, degrading single-venue Hawkes kernel identification.
- Fee hurdle: taking liquidity on sub-minute horizons frequently incurs taker fees that exceed the expected alpha from the core-reaction dislocation $\Delta_t$.

## Falsification plan

1. **Hurst Parameter Consistency Test:** Estimate $H_0$ from tick-level order flow across 10 cryptocurrency perpetuals and 10 liquid equity pairs. Falsification threshold: If the empirical impact exponent $\hat{\alpha}$ deviates significantly from $2 - 2\hat{H}_0$ (difference $> 0.15$ with $p < 0.01$), reject the two-layer Hawkes scaling theory.
2. **Out-of-Sample Return Predictability Test:** Run out-of-sample regressions of future 10-second to 5-minute price returns on the structural dislocation signal $\Delta_t$ vs. standard Order Flow Imbalance ($\text{OFI}_t$). Falsification threshold: If $\Delta_t$ fails to achieve a statistically significant positive coefficient ($t\text{-stat} < 2.0$) or fails to outperform raw OFI in $R^2$, reject the two-layer decomposition advantage.
3. **Net Cost-Aware Execution Audit:** Test the strategy under realistic taker fees (e.g. 2 bps). Falsification threshold: If net Sharpe ratio after fees is non-positive across a 6-month continuous sample, reject live tradability for active taker execution.

## Crypto portability

- **Adapted / Unproven:**
  - The theoretical derivation originates in general market microstructure (tested primarily on liquid equity/futures TAQ data).
  - Porting to crypto perpetuals is direct at the mechanism level (L3 order book dynamics and continuous trading), but requires adaptation to crypto-specific properties: 24/7 trading without market open/close auctions, higher retail noise trader proportions, and cross-exchange liquidity fragmentation.
  - Must be treated as unproven empirical alpha in crypto until validated against raw exchange WebSocket trade feeds.

## Limitations

- **Not independently reproduced:** Based on Muhle-Karbe et al. (2026) theoretical proofs and empirical calibrations.
- **Computational Complexity:** Real-time continuous estimation of multi-dimensional Hawkes processes with power-law kernels requires efficient recursive approximations (e.g. multi-exponential sums).
- **Microstructure Contamination:** Spoofing and latency-arbitrage toxicity can distort the identification of true core metaorders vs. manipulative order cancellations.

## Implementation status

- `not-implemented`
- Research capture only. No implementation in NautilusTrader, PyBroker, or live order routing engines.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Not approved for paper, testnet, or live trading.

## Related Wiki records

- `[[crypto-multilevel-order-flow-imbalance-intraday-2026-08-31]]`
- `[[hawkes-self-exciting-lob-return-sign-forecasting-coe-2026-09-02]]`
- `[[crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31]]`
- `[[passive-market-impact-optimal-execution-mlofi-2026-09-02]]`
- `[[sequential-lob-heavy-tailed-liquidity-crossover-depth-2026-09-02]]`

## Sources

1. Johannes Muhle-Karbe, Youssef Ouazzani Chahdi, Mathieu Rosenbaum, Grégoire Szymanski, *"A Unified Theory of Order Flow, Market Impact, and Volatility"*, arXiv preprint `arXiv:2601.23172v1 [q-fin.TR, q-fin.ST]`, January 30, 2026, revised February 2, 2026. DOI: [10.48550/arXiv.2601.23172](https://doi.org/10.48550/arXiv.2601.23172). Stable URL: https://arxiv.org/abs/2601.23172.
