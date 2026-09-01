---
schema: strategy-research-record-v1
title: "Path Portfolio Optimization: Geometricity Defect, Execution Lift Invariance, and Dimensional Shrinkage"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - portfolio-optimization
  - path-signatures
  - rough-paths
  - stochastic-portfolio-theory
  - excess-growth-rate
  - execution-lift
  - shrinkage-estimators
  - tensor-algebra
  - levy-area
status: research-only
confidence: high
source_as_of: 2026-08-03
sources:
  - "Miquel Noguer i Alonso, 'Path Portfolio Optimization: Defect, Lift, and the Price of Path Complexity', arXiv:2608.02355v1 [q-fin.PM], August 3, 2026. DOI: 10.48550/arXiv.2608.02355. https://arxiv.org/abs/2608.02355"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Path Portfolio Optimization: Geometricity Defect, Execution Lift Invariance, and Dimensional Shrinkage

## Provenance

- **Primary Source:** Miquel Noguer i Alonso (Artificial Intelligence Finance Institute / New York University), *"Path Portfolio Optimization: Defect, Lift, and the Price of Path Complexity"*, arXiv preprint `arXiv:2608.02355v1 [q-fin.PM]`, submitted August 3, 2026. Full text: [https://arxiv.org/html/2608.02355v1](https://arxiv.org/html/2608.02355v1).
- **Primary Categories:** Portfolio Management (`q-fin.PM`), Machine Learning (`cs.LG`), Probability (`math.PR`), Numerical Analysis (`math.NA`).
- **Context:** Foundational path-first portfolio theory formalizing path-dependent asset allocation via truncated tensor algebras of path signatures $\mathbb{S}^{\le m}(X)_{0,T}$, bridging Stochastic Portfolio Theory (Fernholz), signature-linear trading systems, and high-dimensional shrinkage estimators.

## Economic mechanism

### Source-reported

Classical portfolio theory (Markowitz, 1952) treats static weights $\pi$ and covariance matrices $\Sigma$ as primitives, forcing path-dependent features (momentum, cross-asset lead-lag, volatility clustering, drawdown control) to be treated as ad hoc external signals.

Noguer i Alonso (2026) develops *path portfolio optimization*, making the continuous price path $X: [0, T] \to \mathbb{R}^d$ and its path signature $\mathbb{S}(X)_{0,T}$ the universal primitive coordinates. A signature-linear portfolio of truncation level $m$ is $G_\ell(X) = \langle \ell, \mathbb{S}^{\le m}(X)_{0,T} \rangle$.

The paper proves four foundational mathematical and economic theorems:
1. **Geometricity Defect as Risk (Proposition 3, Corollary 6):** The covariance of signature coordinate payoffs is identical to the *defect form*:
   $$D(u, v) = \langle u \sqcup v, \mathbb{E}[\mathbb{S}(X)] \rangle - \langle u, \mathbb{E}[\mathbb{S}(X)] \rangle \langle v, \mathbb{E}[\mathbb{S}(X)] \rangle$$
   Risk is literally the failure of the expected signature $\mathbb{E}[\mathbb{S}(X)]$ to be group-like. When paths are deterministic, $D \equiv 0$.
2. **Fernholz's Excess Growth as Geometricity Defect (Theorem 12, Corollary 13):** The gap between the Marcus (geometric) lift $\mathbb{S}^M$ and forward (Itô iterated sums) lift $\mathbb{S}^F$ at level two is exactly half the quadratic covariation: $\mathbb{S}^{M,ij} - \mathbb{S}^{F,ij} = \frac{1}{2}[X^i, X^j]_T$. When contracted with constant portfolio weights $\pi$, this lift gap is identically Fernholz's excess growth rate:
   $$\gamma^*_\pi = \frac{1}{2} \left(\pi^\top \text{diag}(\Sigma) - \pi^\top \Sigma \pi\right)$$
   Stochastic Portfolio Theory's central rebalancing premium is proved to be the geometricity defect of the portfolio execution map.
3. **Lift Invariance of Direction vs Ruin (Corollaries 14, 15):** The antisymmetric level-2 block (Lévy area / lead-lag: $\frac{1}{2}(X^i dX^j - X^j dX^i)$) is pathwise identical under both Marcus and forward lifts ($6.5 \times 10^{-16}$ numerical discrepancy). Directional and cross-sectional lead-lag signals are completely execution-convention free. In contrast, symmetric blocks (quadratic variation) and solvency/ruin depend strictly on the lift convention: forward-lifted wealth can be extinguished by a single jump ($1 + \pi^\top(e^u - 1) \le 0$), whereas Marcus-lifted continuous wealth cannot.
4. **The Dimensional Price of Path Complexity (Section 6, Propositions 20–22):** 
   - *Oracle Advantage:* Admitting level-2 quadratic path functionals raises oracle certainty equivalent by $11.15\times$ for an asset pair ($d=2, p=6$) and $59.64\times$ for a 20-asset cross section ($d=20, p=420$).
   - *Sample Degradation:* Unregularized sample plug-in $\hat{\ell} = (\gamma \hat{D})^{-1}\hat{\mu}$ collapses catastrophically when sample size $M$ is below $\sim 6$ paths per parameter ($M/p < 6$). At $M/p = 1.19$, the median realized certainty equivalent is $-306\times$ the oracle value.
   - *Regularization & Recovery:* Ridge shrinkage with Marchenko-Pastur ambiguity radius $\delta = \sqrt{p/M}$ or model-consistent generator estimation restores $0.58\times$ to $0.95\times$ oracle value at $M/p \approx 1.19$.

### Research interpretation

This research clarifies where statistical edge in path-dependent multi-asset systematic strategies originates:
1. **Symmetric vs Antisymmetric Separation:** In time-reversible markets with zero expected Lévy area, the entire $59.6\times$ level-2 gain comes from the symmetric block $\frac{1}{2} \Delta X \otimes \Delta X$ (convexity / volatility dispersion harvest), not path forecasting. Path-dependent directional trading pays only when cross-asset drivers exhibit non-zero expected Lévy area (asymmetric Hawkes sign excitation).
2. **Mandatory Shrinkage in Cross-Sectional Alpha:** Expanding trading signals into quadratic/tensor path interactions without eigenvalue shrinkage creates severe out-of-sample overfit and negative certainty equivalent.

## Signal

### 1. Feature Map & Word Indexing
Let $X_t \in \mathbb{R}^d$ be log-prices over horizon $[0, T]$.
- Truncation level $m=2$: parameter count $p = d + d^2$.
- Coordinate words: $w \in \{(i), (ij) : 1 \le i, j \le d\}$.
- Signature coordinates:
  $$\mathbb{S}^i(X)_{0,T} = X_T^i - X_0^i$$
  $$\mathbb{S}^{ij}(X)_{0,T} = \int_0^T (X_t^i - X_0^i) dX_t^j$$
- Decomposition into symmetric (convexity) and antisymmetric (Lévy area) components:
  $$\text{sym}(\mathbb{S}^{ij}) = \frac{1}{2} \mathbb{S}^i \mathbb{S}^j = \frac{1}{2}(X_T^i - X_0^i)(X_T^j - X_0^j)$$
  $$\text{anti}(\mathbb{S}^{ij}) = A^{ij}_{0,T} = \frac{1}{2} \int_0^T \left( (X_t^i - X_0^i) dX_t^j - (X_t^j - X_0^j) dX_t^i \right)$$

### 2. Defect Form Construction
Given estimated mean signature $\hat{\mu}_w = \frac{1}{M}\sum_{k=1}^M \langle w, \mathbb{S}(X^{(k)})\rangle$:
$$\hat{D}(u, v) = \frac{1}{M}\sum_{k=1}^M \langle u \sqcup v, \mathbb{S}(X^{(k)})\rangle - \hat{\mu}_u \hat{\mu}_v$$
where $\sqcup$ is the tensor shuffle product.

### 3. Regularized Path Portfolio Allocator
For risk aversion $\gamma > 0$:
- **Marchenko-Pastur Ridge Shrinkage:**
  $$\hat{D}_{\text{ridge}} = \hat{D} + \sqrt{\frac{p}{M}} \cdot \left(\frac{\text{tr}(\hat{D})}{p}\right) I_p$$
- **Optimal Weight Vector:**
  $$\ell^* = \frac{1}{\gamma} \hat{D}_{\text{ridge}}^{-1} \hat{\mu}$$
- **Second-Order Kelly Scaling:**
  $$\ell^*_{\text{Kelly}} = \frac{1}{1 + \|\hat{D}^{-1/2} \hat{\mu}\|^2} \hat{D}^{-1} \hat{\mu}$$

### 4. Dynamic Execution Rule
Portfolio allocation at time $t \in [0, T]$ is the dynamic feedback:
$$\pi_t^j = \ell_{(j)}^* + \sum_{i=1}^d \ell_{(ij)}^* (X_t^i - X_0^i)$$

## Required data

- **Universe:** Cross-section of $d$ liquid perpetual contracts (e.g., Top 20 Binance/Bybit perps: BTC, ETH, SOL, BNB, etc.).
- **Timeframe:** High-frequency intraday snapshots (1-second to 1-minute sampling) aggregated over trading windows of length $T$ (e.g., 1-hour or 4-hour rebalance horizons).
- **Fields:** Log-prices $X_t^i = \ln(P_t^i / P_0^i)$, trade volume, and timestamps.
- **Point-in-Time Considerations:** Signatures must be computed using causal strictly backward-looking path partitions without forward leakage.

## Execution assumptions

- **Execution Conventions:**
  - Forward lift (Itô discrete execution) applies to real-world order routing.
  - Marcus lift is used for coordinate transformation and continuous theoretical bounds.
- **Transaction Costs & Turnover:** Signature level-2 controls incur dynamic rebalancing costs as price paths evolve. Turnover penalty must be subtracted: $\Delta \text{CE} = -\lambda_{\text{fee}} \sum_{t} \|\pi_t - \pi_{t-1}\|_1$.
- **Slippage & Impact:** Square-root market impact applied to rebalancing trades.

## Evidence

### Source-reported

- **Numerical Invariants:**
  - Closed-form vs Monte Carlo expected signature on 200,000 simulated paths: $\mathbb{E}[\mathbb{S}^1] = 0.060000$ vs $0.060126$; $\mathbb{E}[\mathbb{S}^{12}] = 0.006600$ vs $0.006738$.
  - Defect form reproduces empirical sample covariance with maximum relative error $0.0036$.
  - On deterministic paths, defect form evaluates to $2.78 \times 10^{-17}$ (verifying Corollary 6).
  - Pathwise shuffle identity verified to $2.0 \times 10^{-15}$ precision; Chen concatenation to $6.7 \times 10^{-16}$.
- **Lift Gap Verification:** Marcus vs Forward difference on 20,000 paths of 1,000 steps equals $\frac{1}{2}\Sigma T$ to $10^{-5}$ maximum error; pure-jump difference verified to $1.7 \times 10^{-15}$.
- **Cross-Sectional CE Gains (Oracle):**
  - Asset pair ($d=2, p=6$): $11.15\times$ baseline certainty equivalent.
  - Cross section ($d=20, p=420$): $59.64\times$ baseline certainty equivalent (14.06 from diagonal words, 2.91 from off-diagonal, 59.64 jointly super-additive).
- **Estimation Breakdown & Shrinkage (Sample-Size Floor):**
  - At $d=20, p=420$, raw plug-in at $M=500$ ($M/p = 1.19$) has median $\text{CE} = -306\times$ oracle value ($\text{IQR} = [-634, -402]$).
  - Fixed ridge ($\delta = 0.25$) delivers $+0.58\times$ oracle at $M=500$.
  - Model-consistent generator estimator delivers $+0.95\times$ oracle at $M=500$.

### Independently reproduced

- Not independently reproduced.

### Negative evidence

- None identified in the reviewed sources; absence is not evidence of no negative result.
- Explicit structural negative result documented by author: The antisymmetric block (Lévy area) earns zero premium under time-reversible Brownian drivers and produces non-zero trading profits only when drivers have non-zero expected area (e.g., asymmetric Hawkes sign excitation). Activity excitation without direction ($t=15.99$ on counting path) yields zero edge on price paths ($t=0.96$).

## Falsification plan

1. **Lévy Area Asymmetry Test:** Measure sample cross-area $\hat{A}^{ij}_{0,T} = \frac{1}{2}\int (X^i dX^j - X^j dX^i)$ across pairs of crypto assets (e.g., BTC vs Altcoins).
   - *Falsification Condition:* If empirical mean cross-area is statistically indistinguishable from zero ($t$-stat $< 2.0$) across all market regimes, the hypothesis that path-dependent lead-lag delivers directional alpha is falsified.
2. **Shrinkage Boundary Test:** Compare out-of-sample Sharpe of raw plug-in vs Marchenko-Pastur ridge $\hat{D}_{\text{ridge}}$ at varying sample ratios $M/p \in [0.5, 10.0]$.
   - *Falsification Condition:* If raw plug-in does not exhibit catastrophic collapse at $M/p < 2.5$, the analytical sample-complexity barrier is refuted.
3. **Lift Ruin Verification:** Simulate jump-diffusion price paths with $-30\%$ market gaps.
   - *Falsification Condition:* If forward-lifted continuous-time portfolio models fail to show insolvency when geometric Marcus models remain solvent, the execution lift gap theorem is falsified.

## Crypto portability

- **Interpretation:** Adapted / Unproven for Crypto Portfolio Optimization (theory demonstrated in continuous semimartingale/jump simulations).
- **Portability Characteristics:**
  - *Cross-Sectional Perp Momentum & Lead-Lag:* Direct application to multi-asset crypto portfolios. High cointegration and lead-lag dynamics between BTC/ETH and high-beta altcoins make level-2 signature tensors ideal coordinate systems.
  - *Funding & Gap Risk:* The paper's distinction between Marcus (continuous) and Forward (discrete jump) lifts is critically relevant in crypto, where liquidation cascades create discrete price gaps that can bankrupt levered portfolios.
  - *24/7 High-Frequency Data:* Large sample sizes ($M$) are rapidly accumulated in 24/7 crypto markets, accelerating convergence across the $M/p$ threshold.

## Limitations

- **Simulated Calibration:** Numerical findings in paper are based on calibrated synthetic jump-diffusion and Hawkes processes; empirical market friction and microstructure noise were not modeled.
- **Quadratic Parameter Growth:** Level-2 word count $p = d + d^2$ scales quadratically; for $d=100$ assets, $p = 10,100$, requiring massive sample history ($M > 25,000$) or aggressive structured shrinkage.
- **Execution Latency & Fees:** Intraday continuous signature rebalancing generates high turnover that may erode the level-2 convexity premium under realistic taker fees.

## Implementation status

- `not-implemented`: Research capture only. No production code or backtesting implementation has been executed in the research repository.

## Adoption boundary

- Research-only. Not approved for implementation, paper trading, testnet, or live deployment.

## Related Wiki records

- `[[quant/neural-shrinkage-indefinite-pairwise-correlation-matrix-2026-09-02]]`
- `[[quant/observable-matrix-dynamics-portfolio-optimization-2026-09-02]]`
- `[[quant/hawkes-driven-otc-market-making-volterra-riccati-2026-09-01]]`

## Sources

- Miquel Noguer i Alonso, *"Path Portfolio Optimization: Defect, Lift, and the Price of Path Complexity"*, arXiv preprint `arXiv:2608.02355v1 [q-fin.PM]`, August 3, 2026. DOI: `10.48550/arXiv.2608.02355`. URL: [https://arxiv.org/abs/2608.02355](https://arxiv.org/abs/2608.02355).
- E. Robert Fernholz, *"Stochastic Portfolio Theory"*, Springer-Verlag, New York, 2002.
- Terry Lyons and Weixin Yang, *"Hyperbolic Development and Inversion of Path Signatures"*, arXiv:2208.00560, 2022.
- Christa Cuchiero and J. Möller, *"Universal Portfolio Theory with Path Signatures"*, arXiv preprint, 2024.
