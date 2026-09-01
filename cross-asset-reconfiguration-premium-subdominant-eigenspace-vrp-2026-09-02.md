---
schema: strategy-research-record-v1
title: "Co-Movement Reconfiguration Premium: Subdominant Eigenspace Rotation as an Unspanned Dimension of the Variance Risk Premium"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - variance-risk-premium
  - correlation-geometry
  - principal-angles
  - eigenspace-rotation
  - unspanned-state-variables
  - volatility-forecasting
status: research-only
confidence: medium
source_as_of: 2026-08-20
sources:
  - "Lucas Carvalho, 'The Reconfiguration Premium: Co-movement Structure as an Unspanned Dimension of the Variance Risk Premium', arXiv:2608.20020v1 [q-fin.MF, q-fin.PR, q-fin.ST], August 20, 2026. DOI: 10.48550/arXiv.2608.20020. https://arxiv.org/abs/2608.20020. Code: https://github.com/lucas-p-carvalho/rec-anatomy"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Co-Movement Reconfiguration Premium: Subdominant Eigenspace Rotation as an Unspanned Dimension of the Variance Risk Premium

## Provenance

- **Primary Source:** Lucas Carvalho, *"The Reconfiguration Premium: Co-movement Structure as an Unspanned Dimension of the Variance Risk Premium"*, arXiv preprint `arXiv:2608.20020v1 [q-fin.MF, q-fin.PR, q-fin.ST]`, published August 20, 2026.
- **Canonical DOI:** [10.48550/arXiv.2608.20020](https://doi.org/10.48550/arXiv.2608.20020).
- **Traceable Source URL:** `https://arxiv.org/abs/2608.20020` / `https://arxiv.org/html/2608.20020v1`.
- **Public Replication Repository:** `https://github.com/lucas-p-carvalho/rec-anatomy`.
- **Core Dataset:** Monthly total returns of S&P 500 constituents (June 1994 to December 2025; 379 months $\times$ 430 surviving long-history firms; effective cross-section averaging 421 names per 12-month window), paired with Cboe VIX (`VIXCLS`), Cboe Implied Correlation Indices (`COR1M`, `COR3M`), and Cboe Dispersion Index (`DSPX`).

## Economic mechanism

### Source-reported

Every multi-asset risk model, statistical arbitrage book, and factor portfolio assumes a structural map of the market derived from the equity correlation matrix $C_t = V_t \Lambda_t V_t^\prime$. Existing asset-pricing literature prices only functionals of eigenvalues $\Lambda_t$ (index variance, average pairwise correlation, absorption ratio, implied correlation). These level metrics are invariant to rotations of the eigenbasis $V_t$.

The paper isolates and prices $\dot{V}_t$—the rotational motion of the eigenbasis itself. By stripping the leading market mode (which is near-uniform and positive across windows) and focusing on the three-dimensional subdominant invariant subspace (modes 2 through 4), the author defines the **Reconfiguration Index ($REC$)** as the mean squared sine of principal angles between consecutive 12-month subdominant eigenspaces.

The source reports three core economic findings:
1. **Strong Pricing Coupling:** $REC$ robustly couples to the aggregate variance risk premium ($t = +5.40$, Newey-West 12 lags; $R^2 = 0.504$), even after strictly controlling for volatility and correlation levels.
2. **Unspanned Information:** $REC$ is orthogonal to standard level measures ($\max |r| \le 0.316$ with VIX, $\approx 0.00$ with average correlation), and the traded implied-correlation surface spans only $5.0\%$ to $6.7\%$ of its variation.
3. **Prepayment Mechanism:** Elevated reconfiguration triggers an immediate surge in option-implied variance, while the corresponding realized volatility arrives 2 to 3 quarters later ($h = 1 \dots 9$ months forward, $p < 0.03$). The premium widens upon structural reorganization as an advance payment ("prepaid fear") for anticipated future turbulence, compressing as the turbulence materializes.

### Research interpretation

The priced object is not random estimation wobble or discrete sector substitution, but continuous, diffuse drift in factor loadings ($\dot{B}_t$)—the rate at which market participants rewrite which firms cluster together (crowding turnover). When institutional investors experience rapid restructuring in cross-asset co-movement, option market makers demand elevated variance premiums to bear unhedgeable basis and correlation-breakdown risk.

In quantitative strategy terms, $REC$ serves as a **macro structural conditioning variable** for volatility harvesting:
- When implied volatility is elevated *with* high structural reconfiguration, option markets are pricing visible, well-founded structural shifts; historically, this premium has been safely harvested (64% of 27-year cumulative premium is concentrated in the highest-rotation quartile with only a 15% loss frequency).
- When implied volatility is elevated *without* reconfiguration (unexplained panic or exogenous shock), variance selling experiences severe tail drawdowns.

## Signal

### 1. Dual-Gram Subspace Construction

For a 12-month estimation window ($T = 12$) ending at month $t$:
- Let $R_t \in \mathbb{R}^{T \times N_t}$ be the monthly return matrix of $N_t$ names with full observations in the window.
- Standardize $R_t$ column-by-column to zero mean and unit variance, yielding $Z_t \in \mathbb{R}^{T \times N_t}$.
- Because $T \ll N_t$, compute the $T \times T$ dual-Gram matrix:
  $$G_t = \frac{1}{N_t} Z_t Z_t^\prime$$
- Extract eigenvalues and orthonormal eigenvectors of $G_t$. Project to stock space to recover loadings for subdominant modes $k \in \{2, 3, 4\}$ (excluding market mode 1):
  $$Q_t = \frac{1}{\sqrt{N_t}} Z_t^\prime V_t^{\text{dual}} (\Lambda_t^{\text{dual}})^{-1/2} \in \mathbb{R}^{N_t \times K}, \quad K = 3$$
  where $Q_t^\prime Q_t = I_K$.

### 2. Principal Angle Calculation

- Identify common constituent names $\mathcal{C}_t = \text{cols}(Q_{t-1}) \cap \text{cols}(Q_t)$.
- Restrict $Q_{t-1}$ and $Q_t$ to $\mathcal{C}_t$, re-orthonormalize to obtain $A, B \in \mathbb{R}^{|\mathcal{C}_t| \times K}$.
- Compute singular values of $A^\prime B$:
  $$\sigma_1 \ge \sigma_2 \ge \sigma_3 = \text{svd}(A^\prime B) = \cos \theta_i, \quad i \in \{1, 2, 3\}$$
- Compute raw Reconfiguration Index:
  $$REC_t = \frac{1}{K} \sum_{i=1}^K \sin^2 \theta_i = 1 - \frac{1}{K} \sum_{i=1}^K \sigma_i^2$$
- Compute primary persistent signal via 3-month simple moving average:
  $$\widetilde{REC}_t = \frac{1}{3} \sum_{j=0}^2 REC_{t-j}$$
- Standardize $\widetilde{REC}_t$ using an expanding historical window ($z_t = \frac{\widetilde{REC}_t - \mu_t}{\sigma_t}$) with a minimum 36-month burn-in and clipping at $\pm 2.0$.

### 3. Systematic Conditioning Signal for Variance Harvesting

- **Conditioning Rule:**
  - **High-Reconfiguration Regime ($z_t \ge 0.50$ or top quartile):** Allocate full target weight to short index variance (e.g., selling 1-month ATM straddles / variance swaps delta-hedged).
  - **Low-Reconfiguration / Unexplained Stress Regime ($z_t < 0.0$ and $\text{VIX} > \text{median}$):** Throttle or exit short variance exposure to avoid exogenous crash losses.

## Required data

- **Universe:** Cross-section of large-cap equities (e.g., S&P 500 constituents) or crypto liquid basket (e.g., Top 50 liquid tokens).
- **Timeframe / Horizon:** Monthly returns for correlation Gram matrix ($T = 12$ months lookback); daily/monthly closing prices for realized volatility; 1-month implied volatility (VIX / Deribit DVOL).
- **Fields:**
  - Total returns $R_{i, t}$ per asset.
  - Implied volatility index ($\text{IV}_t = \text{VIX}_t / 100$).
  - Option-implied correlation index ($\text{COR1M}_t$, $\text{COR3M}_t$, $\text{DSPX}_t$).
  - 12-month equal-weighted constituent realized volatility ($\text{RV}_t$).
- **Point-in-Time Alignment:** Month-end execution; $REC_t$ is computed using returns strictly up to month $t$; no future look-ahead.

## Execution assumptions

- **Execution Timing:** Month-end close rebalancing.
- **Order Model:** Market-on-close / TWAP at month-end.
- **Payoff Accounting:** Variance harvest payoff defined as $\text{IV}_t^2 - \text{RV}_{t+1}^2$.
- **Transaction Costs & Slippage:** Excluded in primary empirical decomposition (noted as an attribution model; live trading requires pricing delta-hedging transaction costs, option bid-ask spreads, and variance swap convexity corrections).

## Evidence

### Source-reported

All figures below are directly reported by Lucas Carvalho (arXiv:2608.20020v1, August 2026) based on 368 twelve-month windows (June 1995 to December 2025, 365 regression observations):

1. **Reconfiguration Index Baseline Properties:**
   - Raw $REC$ mean = $0.194$, std = $0.119$, min = $0.005$, max = $0.526$ (July 2002).
   - A typical month rewrites $\approx 19.4\%$ (approx 26-degree turn) of the subdominant 3D classification frame and carries $\approx 80.6\%$ forward.
   - Spectral validation: Modes 2 and 3 sit above the refitted Marchenko-Pastur edge ($1.022$) in essentially 100% of windows; mode 4 in 25%.
   - Davis-Kahan mechanical channel (spectral gap compression) explains only $12.1\%$ ($R^2 = 0.121$) of index variance ($t = -3.14$ upper gap, $t = -2.15$ lower gap); pricing coupling remains invariant at $t = +4.92$ when controlling for all mechanical gap variables.

2. **VRP Coupling Regression:**
   - Baseline log-premium specification: $\log(\text{VIX}_t^2) - \log(\text{RV}_t^2) = \alpha + \beta \widetilde{REC}_t + \gamma_1 \text{vix}_t + \gamma_2 \bar{\rho}_t + \epsilon_t$.
   - $\hat{\beta} = +0.195$, Newey-West standard error = $0.036$, $t = +5.40$, $95\%$ CI $[0.124, 0.266]$, $R^2 = 0.504$ ($n = 365$).
   - Raw unsmoothed index: $\hat{\beta} = +0.126$, $t = +4.02$, $R^2 = 0.456$.
   - Levels specification: $t = +3.21$, $R^2 = 0.149$.

3. **Orthogonality & Spanning:**
   - Correlations: with $\bar{\rho}$ (average pairwise correlation) = $+0.005$; with Realized Vol = $-0.012$; with VIX = $+0.316$.
   - Traded implied correlation surface ($\text{COR1M}, \text{COR3M}, \text{DSPX}$) spans only $5.0\%$ to $6.7\%$ of $REC$ variance ($R^2 = 0.050 - 0.067$).
   - Term structure reaction: Regressing $\text{COR3M} - \text{COR1M}$ slope on $\widetilde{REC}_t$ yields $t = -3.46$ ($\hat{\beta} = -0.910$).

4. **Prepayment Forward Realized Volatility Profile:**
   - Regressing forward log realized variance $\log(\text{RV}_{t+h}^2)$ on $\widetilde{REC}_t$ with $\text{AR}(2)$ lags clears the simulated null at every horizon $h \in [1, 9]$ ($p \le 0.027$), peaking at $h = 7 - 8$ months ($\hat{\beta} = +0.155$, approx $+17\%$ variance increase).

5. **Variance Harvest Attribution:**
   - Over 329 months (July 1998 to November 2025), $64\%$ of cumulative variance premium is concentrated in the highest rotation quartile (Q4).
   - Loss frequency in Q4 is $15\%$ (vs $29\%$ in Q1-Q3); mean loss conditional on loss falls by $60\%$; worst single-month drawdown improves from $-0.099$ to $-0.032$.

### Independently reproduced

Not independently reproduced.

### Negative evidence

The author explicitly documents and pre-registers three decisive negative boundaries:
1. **No Timing Alpha ($t = -1.85$):** Scaling exposure to short variance by expanding-window standardized $REC$ ($1 + 0.5 z_t$) yields a paired $t = -1.85$ against unconditional exposure (Sharpe ratio drops from $1.49$ to $1.36$). Real-time top-quartile rule yields $t = -0.81$ to $-2.23$. $REC$ is a structural conditioning variable, not a standalone timing alpha.
2. **No Crash Protection:** The worst $5\%$ of short-variance payoff months exhibit below-average rotation ($\bar{z} = -0.47$). $REC$ anticipatory power applies to endogenous structural shifts, not exogenous crash events (e.g., Lehman Oct 2008 had ordinary rotation).
3. **Downside Semicovariance Inseparability:** An alternative index built from downside semicovariance collapses to $t = +0.08$ to $+0.21$ once cross-sectional breadth and realized semivariance controls are included; downside structure is collinear with downside intensity at monthly resolution.

## Falsification plan

1. **Cross-Sectional Random Permutation Null:** Shuffle constituent returns cross-sectionally within each month (preserving cross-sectional variance and market mode while destroying firm-specific identity and persistent subspace orientation). If the resulting shuffled index produces a VRP coupling $t > 2.50$, the original result is an artifact of cross-sectional dispersion.
2. **Subspace Dimension Perturbation ($K \in [1, 10]$):** Coupling $t$-statistic must peak at $K = 2 - 4$ (signal modes) and monotonically dilute toward zero for $K \ge 5$ (Marchenko-Pastur bulk). Failure of bulk dilution falsifies the spectral identification.
3. **Out-of-Sample Prepayment Window:** Evaluate $REC$ forward realized volatility forecasting on post-2025 data. If the forward hump-shaped predictability at $h = 3 - 8$ months fails ($p > 0.15$), the prepayment mechanism is rejected.
4. **Transaction Cost & Convexity Stress:** Simulate a dynamic variance-swap replication portfolio with realistic strike-spread slippage and borrow costs. If transaction costs eliminate $> 80\%$ of the Q4 harvest concentration, the conditioning value is non-operational.

## Crypto portability

**Portability Status:** `adapted` / `unproven`.

- **Crypto Mechanism Mapping:**
  - In cryptocurrency markets, cross-asset correlation structure between BTC, ETH, and altcoins undergoes rapid regime shifts (e.g., Bitcoin dominance cycles, DeFi / Layer-1 sector rotations, memecoin liquidity suction).
  - The subdominant eigenspace of the top 50 liquid perpetual contracts (modes 2 through 4) captures sector rotation (e.g., Smart Contract Platforms vs Storage vs Privacy vs DeFi) independent of the systemic market beta (mode 1).
- **Portability Challenges & Risks:**
  - **Data Horizon & Listing Churn:** Unlike 30-year equity panels, liquid crypto assets have high survivor churn and short continuous histories (3-5 years). Estimating dual-Gram matrices requires rolling 90-day to 180-day daily windows rather than 12-month monthly windows.
  - **Deribit DVOL & Variance Swap Convexity:** Crypto options implied volatility (Deribit DVOL) is coin-margined (inverse options) or cash-settled USD, with extreme implied-volatility levels (40% to 100%+).
  - **Funding Rate Interplay:** Short perpetual basis / funding carry introduces an additional cash flow dimension absent in equity index variance swaps.

## Limitations

- **Mismatched Leg Definition:** The source paper defines the VRP dependent variable as 1-month implied variance over 12-month equal-weighted constituent realized variance; it does not match standard 1-month traded variance swaps ($|t| \le 1.9$).
- **Survivor-Tilted Estimation Panel:** The 70/80 coverage filter retains 430 long-history names with almost zero in-sample attrition; results describe persistent large-cap equity cross-sections.
- **Unspanned Nature:** Because $REC$ is unspanned by traded correlation instruments ($\le 6.7\%$), it cannot be directly traded via linear correlation swaps or dispersion baskets.
- **Attribution vs Trading Strategy:** The concentration of premium in Q4 does not produce positive alpha under simple linear or step timing overlays ($t < 0$).

## Implementation status

- `not-implemented`: No execution pipeline or backtest has been implemented in PyBroker or NautilusTrader.
- This document is a research-only capture of an external empirical study.

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Approval Scope:** `research-only`.
- A strategy record being present here does not authorize deployment in paper, testnet, or live trading.

## Related Wiki records

- `[[quant/variance-risk-premium-options-2026-08-30]]`
- `[[quant/leakage-safe-validation-purging-embargo-cpcv-2026-08-27]]`
- `[[quant/spxw-0dte-vrp-learning-to-rank-2026-09-01]]`
- `[[quant/crypto-options-implied-correlation-dispersion-2026-08-31]]`

## Sources

1. Lucas Carvalho. *"The Reconfiguration Premium: Co-movement Structure as an Unspanned Dimension of the Variance Risk Premium"*, arXiv preprint `arXiv:2608.20020v1 [q-fin.MF, q-fin.PR, q-fin.ST]`, submitted August 20, 2026. DOI: [10.48550/arXiv.2608.20020](https://doi.org/10.48550/arXiv.2608.20020). URL: [https://arxiv.org/abs/2608.20020](https://arxiv.org/abs/2608.20020). Full text: [https://arxiv.org/html/2608.20020v1](https://arxiv.org/html/2608.20020v1).
2. Public replication repository and scripts: [https://github.com/lucas-p-carvalho/rec-anatomy](https://github.com/lucas-p-carvalho/rec-anatomy).
