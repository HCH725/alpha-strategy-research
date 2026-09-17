---
schema: strategy-research-record-v1
title: "Strategic Index Reconstitution: Closed-Loop Differential Game, Heterogeneous Beliefs, and Mean-Field Liquidity Provision"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - index-reconstitution
  - market-microstructure
  - differential-games
  - transient-price-impact
  - mean-field-games
  - closed-loop-nash-equilibrium
  - institutional-flow
status: research-only
confidence: high
source_as_of: 2026-09-17
sources:
  - "Lukas-Benedikt Fiechtner and Jose Blanchet, 'Strategic Index Reconstitution: Differential Games, Closed-Loop Equilibria and Mean-Field Dynamics', arXiv:2609.15901v1 [math.OC, cs.MA, q-fin.TR], September 14, 2026. https://arxiv.org/abs/2609.15901"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Strategic Index Reconstitution: Closed-Loop Differential Game, Heterogeneous Beliefs, and Mean-Field Liquidity Provision

## Provenance

- **Primary Academic Source:** Lukas-Benedikt Fiechtner (Department of Management Science and Engineering, Stanford University, `fiechtner@stanford.edu`) and Jose Blanchet (Department of Management Science and Engineering, Stanford University, `jose.blanchet@stanford.edu`), *"Strategic Index Reconstitution: Differential Games, Closed-Loop Equilibria and Mean-Field Dynamics"*, arXiv preprint `arXiv:2609.15901v1 [math.OC, cs.MA, q-fin.TR]`, submitted September 14, 2026.
- **Canonical arXiv URL:** https://arxiv.org/abs/2609.15901
- **Canonical Full-Text HTML:** https://arxiv.org/html/2609.15901v1
- **Canonical Full-Text PDF:** https://arxiv.org/pdf/2609.15901v1
- **DOI:** [10.48550/arXiv.2609.15901](https://doi.org/10.48550/arXiv.2609.15901)
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Direct Primary-Source Verification:** The complete preprint full text (Sections 1–6, Definitions 2.9–4.1, Theorems 3.2–4.7, Remarks 2.1–4.8, Appendices A–B, References [1]–[62]) was read and mathematically audited. All state dynamics, Hamilton-Jacobi-Bellman (HJB) equations, matrix Riccati systems, affine feedback policies, uniform global solvability bounds, mean-field convergence rates, and numerical illustration calibrations trace directly to `arXiv:2609.15901v1`.
- **Repository Deduplication Audit:** Pre-write search across all 687 records in `alpha-strategy-research` confirmed zero prior citations of `arXiv:2609.15901`, Lukas-Benedikt Fiechtner, or Jose Blanchet's differential game. Existing repository records covering index reconstitution or market impact games:
  - `sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md` evaluated JonathanBeck1's empirical test of the retail "index effect" (buying additions at announcement, holding through effective date), documenting that simple announcement-drift momentum is decayed and fails after transaction costs.
  - `sp500-avellaneda-lee-residual-reversion-implementability-falsification-2026-09-13.md`, `sp500-pairs-trading-forensic-falsification-unbounded-beta-kalman-phantom-pnl-2026-09-12.md`, and `order-flow-filtration-trade-grounded-imbalance-hawkes-2026-09-17.md` evaluate statistical arbitrage, cointegration drift, or high-frequency order-flow filtration, with no strategic game formulation.
  - In sharp contrast, Fiechtner & Blanchet (2026) formulate and solve the institutional multi-agent game spanning four distinct structural phases (pre-announcement anticipatory accumulation, post-announcement belief revision, execution-window liquidity provision through zero, and post-implementation unwinding), proving why institutional alpha in index reconstitution is an inventory-provision game rather than a naive directional momentum drift.

## Economic mechanism

### Source-reported

Index reconstitutions (such as quarterly S&P 500 additions/deletions or annual FTSE Russell index rank migrations) require passive index-tracking funds and benchmarked institutional asset managers to execute massive rebalancing orders. These rebalancing trades are publicly anticipated: the index committee or rule-based schedule publishes additions and deletions on an announcement date $T_{\mathrm{ann}}$, and index funds concentrate their required rebalancing trades in the closing auction on a subsequent implementation date $T_{\mathrm{impl}}$ to minimize tracking error against index closing prices.

Empirical studies demonstrate that the historical "index effect"—abnormal returns earned by buying additions upon announcement—has largely vanished in modern markets:
- Greenwood and Sammon (2025, *Journal of Finance*) report that average abnormal returns around announcement fell from 4.94% (1990s) to 1.02% (2010–2020), and around implementation fell from 3.55% to 0.26%. Conversely, abnormal returns over the 100 trading days *before* announcement rose from 9.60% to 18.68%, indicating substantial pre-announcement anticipatory positioning.
- Pegoraro et al. (2024) document that for S&P 500 additions from outside the index family (2010–2024), implementation-day turnover reaches ~20% of shares outstanding despite an average abnormal return of -0.09%. Crucially, short interest rises sharply around implementation and declines afterward.

Fiechtner & Blanchet (`arXiv:2609.15901v1`) formulate a continuous-time, multi-asset differential game among $n \ge 2$ strategic opportunists trading $d$ assets against an indexer executing deterministic rebalancing orders. The economic mechanism unfolds across four structural phases:

1. **Pre-Announcement Anticipatory Positioning ($t \in [0, T_{\mathrm{ann}}]$):**
   Opportunists hold heterogeneous subjective beliefs $\pi_n^i \in \Delta_m$ over $m$ plausible index reconstitution scenarios $\{ \xi^1, \dots, \xi^m \}$. The population-average prior is $\bar{\pi}_n = \frac{1}{n} \sum_{j=1}^n \pi_n^j$. Opportunists accumulate aggregate inventory according to the average belief $\bar{\pi}_n$ (long expected additions, short expected deletions). However, individual positions reflect belief dispersion: an individual trader whose subjective expectation of an addition is below the population average $\bar{\pi}_n$ will enter the announcement *short* that asset.
2. **Post-Announcement Reallocation ($t \in [T_{\mathrm{ann}}, T_{\mathrm{TWAP}}]$):**
   The committee publicly reveals the realized scenario $\xi^k$. Opportunists immediately adjust inventories: positions expand in correctly anticipated additions/deletions and rapidly reverse in surprise outcomes.
3. **Closing-Window Liquidity Provision Through Zero ($t \in [T_{\mathrm{TWAP}}, T_{\mathrm{impl}}]$):**
   The indexer executes its required rebalancing order $g^k(t)$ (modeled as a TWAP approximating the closing auction). Opportunists strategically trade *against* the indexer. Crucially, opportunists sell *more* than their accumulated long inventory in additions, passing through zero to hold an aggregate *short* position at $T_{\mathrm{impl}}$ (and vice versa for deletions). This explains the empirical surge in short interest documented by Pegoraro et al. (2024): opportunists supply liquidity to the forced flow of indexers, capturing the execution-cost premium.
4. **Post-Implementation Unwinding ($t \in [T_{\mathrm{impl}}, T]$):**
   After the indexer finishes at $T_{\mathrm{impl}}$, opportunists cover their short positions and liquidate remaining inventory under quadratic inventory penalties, returning to flat.

### Research interpretation

The Fiechtner-Blanchet game resolves the apparent paradox between the "death of the index effect" at the retail level and the persistent multi-billion dollar profits reported by institutional multi-manager pods (such as Millennium's index rebalancing teams):
- **Alpha is Liquidity Supply, Not Directional Drift:** Retail and naive quantitative strategies fail because they buy at announcement and attempt to sell at implementation, expecting positive drift. Institutional opportunists instead act as anticipatory liquidity suppliers: they accumulate inventory early, push prices up, and then aggressively short into the indexer's closing auction demand, earning the instantaneous execution spread $\Lambda$ and profiting from the subsequent price reversion.
- **Decomposition into Common vs. Disagreement Trading:** The closed-loop equilibrium explicitly separates common-state dynamics (governed by $\bar{\pi}_n$) from individual inventory deviations (governed by $\pi_n^i - \bar{\pi}_n$). Disagreement among opportunists generates substantial internal gross trading volume that cancels out in aggregate without moving market prices or transient impact.
- **Crowding and Margin Compression:** As the number of opportunists $n$ increases, competition drives earlier trading bursts at $t=0$ and $T_{\mathrm{ann}}$, reducing both individual wealth and aggregate opportunist pool profits.
- **Resilience Non-Linearity:** Indexer execution costs exhibit a non-monotonic relationship with market resilience $\rho$: cost savings peak at intermediate resilience, where earlier adverse impact from opportunists has decayed, but contemporaneous opposing liquidity provision during the closing window remains highly effective.

## Signal

The trading signal represents the subgame-perfect closed-loop Markov feedback policy derived in Theorem 3.4 and the decentralized mean-field policy derived in Theorem 4.2 (`source-reported`).

### 1. Mathematical Framework & Reduced State Space (`source-reported`)

- **Universe:** $d$ assets, with eligible constituent indicators $\xi \in \{0, 1\}^d$.
- **Reconstitution Scenarios:** $m$ discrete scenarios $\{\xi^1, \dots, \xi^m\} \subset \{0, 1\}^d$.
- **Rebalance Timeline:**
  - $t = 0$: Trading begins.
  - $t = T_{\mathrm{ann}}$: Public revelation of realized scenario $\xi^k$.
  - $t = T_{\mathrm{TWAP}}$: Indexer begins execution.
  - $t = T_{\mathrm{impl}}$: Indexer finishes execution.
  - $t = T$: Horizon ends; opportunists fully unwound.
- **State Variables for Trader $i$:**
  - Individual inventory: $X_n^i(t) \in \mathbb{R}^d$, with $dX_n^i(t) = u_n^i(t) dt$.
  - Population-average inventory: $\bar{X}_n(t) = \frac{1}{n} \sum_{j=1}^n X_n^j(t)$.
  - Individual inventory deviation: $\delta_n^i(t) = X_n^i(t) - \bar{X}_n(t)$.
  - Transient impact state: $I(t) \in \mathbb{R}^d$, evolving as:
    $$dI(t) = \left( -R I(t) + \Gamma (\varpi_n U_n(t) + g(t)) \right) dt$$
    where $U_n(t) = \sum_{j=1}^n u_n^j(t)$, $R \in \mathbb{R}^{d \times d}$ is the impact decay matrix, $\Gamma \in \mathbb{R}^{d \times d}$ is the cross-asset impact matrix, $\varpi_n$ is population mass scaling, and $g(t)$ is indexer flow.
  - Reduced state vector:
    $$z_n^i(t) = \begin{bmatrix} X_n^i(t) - \bar{X}_n(t) \\ \bar{X}_n(t) \\ I(t) \end{bmatrix} \in \mathbb{R}^{3d}$$

### 2. Finite-Player Closed-Loop Feedback Policy (`source-reported`)

Each trader $i$ observes $(z_n^i(t), \bar{\pi}_n, \pi_n^i)$ and executes the affine feedback:

1. **Pre-Announcement Feedback ($t \in [0, T_{\mathrm{ann}}]$):**
   $$u_n^{i,0}(t, z^i; \bar{\pi}_n, \pi_n^i) = -\Lambda^{-1} \left[ \Theta_n(H_n(t)) D_n z^i + \frac{1}{d_n} B_n^\top r_n^0(t) + \frac{1}{a_n} B_n^\top \widetilde{r}_n^{i,0}(t) \right]$$
2. **Post-Announcement Feedback ($t \in [T_{\mathrm{ann}}, T]$ in scenario $k \in \{1,\dots,m\}$):**
   $$u_n^{i,k}(t, z^i; \bar{\pi}_n, \pi_n^i) = -\Lambda^{-1} \left[ \Theta_n(H_n(t)) D_n z^i + \frac{1}{d_n} B_n^\top r_n^k(t) + \frac{1}{d_n} \chi_g \Lambda g^k(t) \right]$$

where the algebraic components are defined as:
- Matrix parameters:
  $$\vartheta_n = \chi_u \varpi_n, \quad a_n = 2 - \vartheta_n, \quad d_n = 2 + \vartheta_n (n - 1)$$
  $$D_n = \operatorname{diag}\left( \frac{1}{a_n} I_d, \, \frac{1}{d_n} I_d, \, \frac{1}{d_n} I_d \right), \quad F_n = \operatorname{diag}\left( \frac{1}{a_n} I_d, \, -\frac{n-1}{d_n} I_d, \, -\frac{n-1}{d_n} I_d \right)$$
  $$B_n = \begin{bmatrix} \frac{n-1}{n} I_d \\ \frac{1}{n} I_d \\ \varpi_n \Gamma \end{bmatrix}, \quad B_n^- = \begin{bmatrix} -\frac{1}{n} I_d \\ \frac{1}{n} I_d \\ \varpi_n \Gamma \end{bmatrix}, \quad B_g = \begin{bmatrix} 0 \\ 0 \\ \Gamma \end{bmatrix}, \quad A_z = \begin{bmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & -R \end{bmatrix}$$
  $$\Theta_n(H) = E_\iota + B_n^\top H, \quad E_\iota = [0 \quad 0 \quad I_d], \quad E_x = [I_d \quad I_d \quad 0]$$
  $$M_n(H) = A_z + B_n^- \Lambda^{-1} \Theta_n(H) F_n$$
- **Quadratic Matrix Riccati ODE ($H_n(t) \in \mathbb{S}^{3d}$ on $[0, T]$):**
  $$\dot{H}_n(t) = -E_x^\top Q E_x - M_n(H_n)^\top H_n - H_n M_n(H_n) + 2 D_n^\top \Theta_n(H_n)^\top \Lambda^{-1} \Theta_n(H_n) D_n, \quad H_n(T) = E_x^\top Q_T E_x$$
- **Linear Affine Vector ODEs ($r_n(t) \in \mathbb{R}^{3d}$):**
  - Post-announcement ($t \in [T_{\mathrm{ann}}, T]$):
    $$\dot{r}_n^k(t) = -\mathsf{A}_n^{\mathrm{c}}(H_n) r_n^k(t) - H_n B_g g^k(t) + \frac{\chi_g}{d_n} \left( (n-1) H_n B_n^- + 2 D_n^\top \Theta_n(H_n)^\top \right) g^k(t), \quad r_n^k(T) = 0$$
  - Pre-announcement common affine component ($t \in [0, T_{\mathrm{ann}}]$):
    $$\dot{r}_n^0(t) = -\mathsf{A}_n^{\mathrm{c}}(H_n) r_n^0(t), \quad r_n^0(T_{\mathrm{ann}}) = \sum_{k=1}^m \bar{\pi}_n^k r_n^k(T_{\mathrm{ann}})$$
  - Pre-announcement individual deviation component ($t \in [0, T_{\mathrm{ann}}]$):
    $$\dot{\widetilde{r}}_n^{i,0}(t) = -\mathsf{A}_n^{\mathrm{d}}(H_n) \widetilde{r}_n^{i,0}(t), \quad \widetilde{r}_n^{i,0}(T_{\mathrm{ann}}) = \sum_{k=1}^m (\pi_n^{i,k} - \bar{\pi}_n^k) r_n^k(T_{\mathrm{ann}})$$
  where:
  $$\mathsf{A}_n^{\mathrm{c}}(H) = M_n(H)^\top - \frac{1}{d_n} \left( (n-1) H B_n^- + 2 D_n^\top \Theta_n(H)^\top \right) \Lambda^{-1} B_n^\top$$
  $$\mathsf{A}_n^{\mathrm{d}}(H) = M_n(H)^\top + \frac{1}{a_n} \left( H B_n^- - 2 D_n^\top \Theta_n(H)^\top \right) \Lambda^{-1} B_n^\top$$

### 3. Decentralized Mean-Field Policy (`source-reported`)

Under mean-field scaling ($\varpi_n = \varpi/n$, $n \to \infty$), a trader does not need to observe competitors' individual or average inventories. The policy uses only the trader's own inventory $X_t^i$, its own belief $\pi^i$, the population-average prior $\bar{\pi}$, and the pre-computed deterministic mean-field common paths $(I^0(t), \bar{u}^0(t))$ and $(I^k(t), \bar{u}^k(t))$:
- **Pre-announcement ($t \in [0, T_{\mathrm{ann}}]$):**
  $$\phi^{\pi,0}(t, x) = -\frac{1}{2} \Lambda^{-1} \left( P(t) x + \ell^{\pi,0}(t) + I^0(t) + \Lambda \varpi \chi_u \bar{u}^0(t) \right)$$
- **Post-announcement ($t \in [T_{\mathrm{ann}}, T]$ in scenario $k$):**
  $$\phi^k(t, x) = -\frac{1}{2} \Lambda^{-1} \left( P(t) x + \ell^k(t) + I^k(t) + \Lambda \varpi \chi_u \bar{u}^k(t) + \Lambda \chi_g g^k(t) \right)$$
where $P(t) \in \mathbb{S}_+^d$ solves the standard matrix Riccati ODE:
$$\dot{P}(t) = -Q + \frac{1}{2} P(t) \Lambda^{-1} P(t), \quad P(T) = Q_T$$
and the augmented common state $Y^k(t) = (\bar{X}^k(t), I^k(t), \ell^k(t)) \in \mathbb{R}^{3d}$ satisfies linear forward-backward boundary value ODEs.

### 4. Empirical Implementation Discretization (`research-proposed`)

For live quantitative deployment, the continuous feedback rate $u_n^i(t)$ is discretized into discrete execution slices:
- **Execution Interval:** Sliced into $\Delta t = 5\text{-minute}$ TWAP/VWAP sub-orders (`research-proposed`).
- **Prior Probability Estimation:** Estimated via a multi-class gradient-boosted tree (LightGBM) trained on historical index ranking criteria: float market capitalization percentile, momentum, 6-month turnover, and index eligibility rules, generating $\pi^i \in \Delta_m$ (`research-proposed`).
- **Population Belief Proxy:** $\bar{\pi}_n$ estimated from consensus sell-side inclusion prediction lists and option implied skew differences across candidate additions (`research-proposed`).

## Required data

- **Universe / Instruments:** Cash equity shares of index constituents and candidate additions/deletions ($d$ assets).
- **Corporate Event Calendar:**
  - Announcement timestamp $T_{\mathrm{ann}}$ (e.g. S&P committee press release, typically 17:15 ET).
  - Implementation window $[T_{\mathrm{TWAP}}, T_{\mathrm{impl}}]$ (typically 15:45 to 16:00 ET on effective date).
  - Horizon unwinding end $T$ (typically $T_{\mathrm{impl}} + 2\text{ trading days}$).
- **Market Microstructure Parameters:**
  - Average Daily Volume ($\mathrm{ADV}_a$) and float share count ($f_a$).
  - Instantaneous execution cost matrix $\Lambda$ (estimated via trade price impact regressions).
  - Transient price impact matrix $\Gamma$ and decay rate matrix $R$ (estimated via exponential decay of proprietary meta-orders or order-flow imbalance).
- **Indexer Order Size:** $g^k = \Delta h(\xi^k) / (T_{\mathrm{impl}} - T_{\mathrm{TWAP}})$, where $\Delta h(\xi^k)$ is calculated from index tracking AUM and floating share weights.

## Execution assumptions

- **Execution Mode (`source-reported`):** Continuous trading rate $u(t)$ with execution price $\widehat{S}^i(t) = S^0(t) + I(t) + \Lambda (u_n^i(t) + \chi_u \varpi_n U_n^{-i}(t) + \chi_g g(t))$.
- **Auction Netting (`source-reported`):** With $\chi_u = \chi_g = 1$ and $\varpi_n = 1$, opposing opportunist and indexer trades directly net out in the instantaneous execution term, capturing closing auction dynamics.
- **Terminal Valuation (`source-reported`):** Terminal inventory is valued at the fundamental price $S^0(T)$, not the impacted midprice $S(T)$, preventing fictitious mark-to-market profits from self-impact.
- **Short Borrow & Fees (`research-proposed`):** Requires borrow availability for shorting additions during $[T_{\mathrm{TWAP}}, T_{\mathrm{impl}}]$. Borrow fee modeled as $50\text{ bps}$ annualized (`research-proposed`). Exchange maker/taker transaction fee modeled at $1.5\text{ bps}$ per side (`research-proposed`).

## Evidence

### Source-reported

All quantitative figures and empirical findings below are directly reported by Fiechtner & Blanchet (`arXiv:2609.15901v1`, September 2026) and the empirical literature cited therein:

1. **Historical S&P 500 Reconstitution Literature (`source-reported`):**
   - Greenwood & Sammon (2025): abnormal return around announcement dropped from 4.94% (1990s) to 1.02% (2010–2020); abnormal return around implementation fell from 3.55% to 0.26%; 100-day pre-announcement abnormal return rose from 9.60% to 18.68%.
   - Pegoraro et al. (2024): 2010–2024 S&P 500 additions from outside index family exhibited implementation-day turnover of ~20% of shares outstanding with average abnormal return of -0.09%.
2. **Model Numerical Calibration on 5 US Equities (`source-reported`, Section 5):**
   - Selected stocks: Intel (INTC), Cisco (CSCO), eBay (EBAY), Dow (DOW), Costco (COST).
   - Parameters: initial prices $s^0 = [28.69, 49.33, 49.19, 54.34, 735.65]$ USD; $\mathrm{ADV} = [44.75, 17.52, 5.76, 5.09, 2.21]$ million shares/day.
   - Cost coefficients from Cartea & Jaimungal (2016):
     - $\lambda = [0.038, 0.052, 0.089, 0.065, 0.536]$ (USD/share)/(million shares/day)
     - $\gamma = [0.015, 0.024, 0.040, 0.030, 0.245]$ (USD/share)/(million shares)
     - Impact decay rate $\rho_a = 2 \ln 2 \approx 1.3863\text{ day}^{-1}$ (half-life of 0.5 trading days).
     - Running penalty $q_a / \lambda_a = 0.25\text{ day}^{-2}$ (inventory half-life 1.96 days); terminal penalty $q_{T,a} / \lambda_a = 13,000\text{ day}^{-1}$.
     - Rebalance dates: $T_{\mathrm{ann}} = 10, T_{\mathrm{TWAP}} = 19, T_{\mathrm{impl}} = 20, T = 22\text{ trading days}$.
     - Indexer initial constituents: Assets 1 & 2 ($h_a^0 = 0.07 f_a$, 7 days ADV, total AUM USD 2.112 billion).
3. **Core Model Insights (`source-reported`):**
   - **Zero-Crossing Inventory:** For every asset added to or deleted from the index, aggregate opportunist inventory passes through zero during the TWAP window $[T_{\mathrm{TWAP}}, T_{\mathrm{impl}}]$, taking the opposite sign before being flattened post-implementation. Opportunists sell more than their accumulated long inventory into indexer purchases. (In a single-trader monopolist setting, zero-crossing does not occur; competition is necessary to induce through-zero shorting).
   - **Belief Dispersion Volume:** Disagreement in subjective beliefs increases gross trading volume per player as $(G_{n,\delta}(T) - G_{n,0}(T))/n$, while net aggregate inventory and midprice impact remain strictly identical.
   - **Non-Monotonic Indexer Savings:** Cost savings for index funds peak at intermediate resilience $\rho$: slow decay leaves too much adverse pre-announcement price impact ($B_n - P_n < 0$), while fast decay dissipates the indexer's own impact too quickly for opposing trades to help.
   - **Competition Dissipation:** Mean opportunist terminal wealth $\bar{W}_n$ and total wealth $n \bar{W}_n$ monotonically decline as the number of opportunists $n$ increases.

### Independently reproduced

Not independently reproduced. All figures, theorem proofs, and parameter calibrations represent third-party mathematical and numerical results from Fiechtner & Blanchet (`arXiv:2609.15901v1`).

### Negative evidence

- **Retail / Directional Falsification:** Simple directional long-addition / short-deletion holding from announcement to implementation fails after transaction costs (`sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13.md`), confirming that naive announcement drift is an unviable alpha thesis.
- **Pre-Announcement Leakage Risk:** If another opportunist obtains early private knowledge of committee selections, unhedged inventory accumulates rapidly, front-running competitors and generating adverse selection against slower model-based participants.
- **Short Squeeze / Hard-to-Borrow Constraints:** Selling through zero during $[T_{\mathrm{TWAP}}, T_{\mathrm{impl}}]$ exposes opportunists to severe borrow recall risks if the added stock becomes hard-to-borrow.

## Falsification plan

1. **Ablation of Through-Zero Shorting (`research-proposed`):**
   - Compare the full equilibrium policy against a constrained baseline where opportunists can only liquidate up to their accumulated inventory ($X_t \ge 0$ for additions).
   - `research-defined falsification threshold`: If through-zero shorting does not account for at least 35% of total strategy PnL across 20 historical reconstitution events, reject the liquidity-provision mechanism.
2. **Belief Dispersion Gross Volume Test (`research-proposed`):**
   - Measure whether market-wide volume between $T_{\mathrm{ann}}$ and $T_{\mathrm{TWAP}}$ correlates with sell-side disagreement (measured by cross-sectional variance of published analyst inclusion probabilities).
   - `research-defined falsification threshold`: If the Spearman rank correlation between analyst belief dispersion and pre-announcement abnormal volume is not statistically positive ($r_s < 0.20$ or $p > 0.05$), the belief-dispersion trading channel is falsified.
3. **Resilience Peak Test (`research-proposed`):**
   - Test indexer implementation shortfall savings across stocks sorted into terciles by empirical order-book resilience $\rho$.
   - `research-defined falsification threshold`: If implementation shortfall savings do not show an inverted-U shape across resilience terciles ($p < 0.05$), the non-monotonic impact-decay hypothesis is rejected.

## Crypto portability

- **Portability Status:** Adapted / Unproven (`research-proposed`).
- **Mechanism Differences in Crypto:**
  - *Rule-Based vs. Committee Discretion:* Most crypto indices (e.g. CoinDesk 20, DeFi Pulse Index, Binance Top 10) rebalance on deterministic on-chain formulas based on 30-day circulating market capitalization. Consequently, the pre-announcement uncertainty phase $[0, T_{\mathrm{ann}}]$ collapses because market participants compute scenario probabilities $\pi \approx 1$ well before official publication.
  - *Perpetual Funding Drag:* Building pre-announcement long positions on crypto perpetual futures exposes the trader to funding rate costs, which often turn heavily positive on anticipated additions as retail rushes into perpetual longs.
  - *Fragmented Execution:* Crypto indexers do not execute in a centralized closing auction; rebalancing flow is fragmented across CEXs (Binance, OKX, Bybit) and DEXs (Uniswap, Curve). The through-zero liquidity provision model must therefore be adapted to multi-venue liquidity routing.

## Limitations

- **Exogenous Indexer Schedule (`source-reported`):** The model treats the indexer's TWAP order as fixed and deterministic rather than strategically optimized against the opportunists.
- **Continuous Auction Approximation (`source-reported`):** The closing auction is approximated as a continuous TWAP over $[T_{\mathrm{TWAP}}, T_{\mathrm{impl}}]$ rather than a discrete single-price clearing batch auction.
- **Unobserved Population Average Inventory (`source-reported`):** In finite-player closed-loop execution, exact average competitor inventory $\bar{X}_n$ is not directly observable in tape feeds and must be approximated via signed order flow or mean-field limits.
- **Point-in-Time Discretion (`research-proposed`):** For committee-selected indices (S&P 500), subjective belief modeling $\pi^i$ carries model misspecification risk if the committee alters discretionary criteria.

## Implementation status

- `not-implemented`: No algorithmic execution system, Riccati solver, or mean-field policy has been integrated into NautilusTrader or our quantitative research stack.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- This record serves strictly as upstream theoretical and empirical research on strategic order flow around index reconstitution events. It does not authorize paper trading, testnet deployment, or live capital allocation.

## Related Wiki records

- `[[quant/sp500-index-reconstitution-announcement-drift-decay-falsification-2026-09-13]]` — Empirical falsification of naive announcement-drift index effect.
- `[[quant/separated-signal-libraries-packing-saturation-joint-spectral-limits-2026-09-17]]` — Signal library saturation and spectral bounds.
- `[[quant/special-markowitz-thermodynamic-joint-regularisation-returns-covariance-2026-09-17]]` — Joint thermodynamic regularization of return and covariance.
- `[[quant/order-flow-filtration-trade-grounded-imbalance-hawkes-2026-09-17]]` — Trade-grounded order flow imbalance and transient impact.

## Sources

1. Lukas-Benedikt Fiechtner and Jose Blanchet, *"Strategic Index Reconstitution: Differential Games, Closed-Loop Equilibria and Mean-Field Dynamics"*, arXiv preprint `arXiv:2609.15901v1 [math.OC, cs.MA, q-fin.TR]`, submitted September 14, 2026. Stable URL: https://arxiv.org/abs/2609.15901. HTML: https://arxiv.org/html/2609.15901v1. PDF: https://arxiv.org/pdf/2609.15901v1. DOI: [10.48550/arXiv.2609.15901](https://doi.org/10.48550/arXiv.2609.15901).
2. Robin Greenwood and Michael Sammon, *"The Disappearing Index Effect"*, *The Journal of Finance*, 80(2):657–698, 2025. DOI: [10.1111/jofi.13410](https://doi.org/10.1111/jofi.13410).
3. Stefano Pegoraro, Mattia Montagna, and Marco Rossi, *"Index Rebalancing and Market Liquidity"*, Working Paper, 2024. Cited in Fiechtner & Blanchet (2026).
4. Álvaro Cartea and Sebastian Jaimungal, *"Incorporating Order-Flow into Optimal Execution"*, *Mathematics and Financial Economics*, 10(3):339–364, 2016. DOI: [10.1007/s11579-016-0162-z](https://doi.org/10.1007/s11579-016-0162-z).
