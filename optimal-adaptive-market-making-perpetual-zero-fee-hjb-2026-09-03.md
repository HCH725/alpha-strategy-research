---
schema: strategy-research-record-v1
title: "Optimal Adaptive Market Making with Cross-Exchange Hedging in Zero-Fee Perpetual Futures"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - crypto
  - perpetual-futures
  - market-making
  - zero-fee
  - stochastic-optimal-control
  - hjb
  - cross-exchange-hedging
  - funding-rate
  - adverse-selection
status: research-only
confidence: medium
source_as_of: 2026-07-16
sources:
  - "https://arxiv.org/abs/2607.11888"
  - "https://doi.org/10.48550/arXiv.2607.11888"
  - "https://arxiv.org/html/2607.11888v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Optimal Adaptive Market Making with Cross-Exchange Hedging in Zero-Fee Perpetual Futures

## Provenance

- **Primary paper:** Minmin Zeng and Yi Liu (tsaftech), *Optimal Adaptive Market Making: A Theoretical Framework for High-Yield Liquidity Provision in Perpetual Futures Markets*, arXiv preprint `arXiv:2607.11888v1 [cs.AI, q-fin.TR, q-fin.PM]`, submitted 16 Jul 2026. DOI: `10.48550/arXiv.2607.11888`.
- **Primary source text:** Complete author-published LaTeX source and figures downloaded from `https://arxiv.org/e-print/2607.11888` (July 2026 snapshot), including `main.tex`, `sections/market_model.tex`, `sections/adverse_selection.tex`, `sections/optimal_mm.tex`, `sections/high_apy.tex`, `sections/zero_fee.tex`, `sections/cross_exchange.tex`, `sections/numerical.tex`, and `sections/appendix.tex`.
- **Public access URL:** https://arxiv.org/abs/2607.11888 and experimental HTML full text at https://arxiv.org/html/2607.11888v1.
- **Source/data as-of:** 2026-07-16.
- **Source-identity deduplication:** Repository-wide audit confirmed zero matching records for `2607.11888`, `Optimal Adaptive Market Making`, `Master APY`, `Minmin Zeng`, `Yi Liu`, or `tsaftech`. Existing market making records in this repository (e.g., `funding-aware-market-making-perpetual-dex-2026-08-31.md` covering Le 2026 / arXiv:2605.06405; `market-making-axiomatic-unified-inventory-quoting-spread-decomposition-2026-09-02.md`; `market-making-latent-fad-stochastic-control-hjb-2026-09-02.md`) address fundamentally different source identities, single-venue formulations, or disparate theoretical questions. Zeng & Liu (2026) uniquely introduces the dual-venue zero-maker-fee DEX vs. CEX framework, cross-exchange basis hedging thresholds under funding rate differentials, and the Master APY Formula.

## Economic mechanism

### Source-reported

The paper investigates the conditions under which an algorithmic market maker (MM) operating on a decentralized perpetual futures exchange (DEX-A) with zero maker fees ($\phi_m^{\mathrm{DEX}} = 0$) can achieve sustained annualized percentage yields (APY) on deployed capital.

The authors identify five foundational economic pillars:
1. **Fee Floor Elimination as an Economic Moat:** On centralized exchanges (CEX-B), maker fees $\phi_m^{\mathrm{CEX}} > 0$ establish a hard spread floor ($\delta \geq \alpha + \phi_m^{\mathrm{CEX}}$) below which quoting is strictly negative expectation. On zero-fee DEX venues, this fee floor vanishes, leaving adverse selection $\alpha$ as the sole binding constraint. This expands the universe of tradeable markets and enables tighter quotes that boost fill arrival rates $\bar{\lambda}$.
2. **PnL Decomposition:** Marked-to-market PnL over interval $[0, T]$ decomposes into five orthogonal channels: (i) cumulative spread income, (ii) adverse selection loss (partitioned into stale-quote latency arbitrage and informed flow), (iii) inventory carrying cost (mark-to-market variance), (iv) cross-exchange hedging friction (taker fees on CEX-B), and (v) venue fee costs (identically zero on the DEX).
3. **Stochastic Optimal Control (HJB):** Under constant absolute risk aversion (CARA) utility of terminal wealth, the MM jointly controls bid/ask half-spreads $(\delta^b, \delta^a)$ and discrete cross-exchange hedging trades $h \in \{0, \pm 1\}$. An inventory penalization approach yields stationary optimal quotes with inventory-independent total spread width.
4. **Cross-Exchange Hedging & Funding Dynamics:** When inventory breaches an optimal threshold $q^*$, the MM hedges on CEX-B. Hedging reduces inventory variance but incurs taker fees $\phi_t^{\mathrm{CEX}}$ and exposes the MM to funding rate differentials $\Delta r_f = r_f^{\mathrm{DEX}} - r_f^{\mathrm{CEX}}$. A hedge viability parameter $\Gamma_h$ establishes a trichotomy: full-hedge ($\Gamma_h > 3$), partial-hedge ($1 < \Gamma_h \leq 3$), and no-hedge ($\Gamma_h \leq 1$).
5. **Master APY Formula & Drawdown Invariance:** Annualized return factors into $\mathrm{APY} = \mathrm{APY}_0 (1 - \xi) (1 - \rho_\Sigma)$, where $\xi = \alpha / \bar{\delta}^*$ is the adverse selection ratio and $\rho_\Sigma = \rho_{\mathrm{inv}} + \rho_{\mathrm{hedge}} + \rho_{\mathrm{fund}}$ is aggregate operational friction. Furthermore, maximum drawdown satisfies an exponential tail bound $\mathbb{P}(\mathrm{MDD} > x) \leq e^{-\theta_{\mathrm{dd}} x}$, revealing that the product $\mathrm{APY} \times \mathrm{VaR}_{95\%}^{\mathrm{MDD}}$ is invariant to leverage.

### Research interpretation

This is an optimal liquidity provision and market microstructure risk-management framework, not a directional forecasting alpha. 

The falsifiable core hypothesis is: **A market maker quoting on a zero-maker-fee perpetual DEX who dynamically adjusts bid/ask skews via inventory-penalized HJB control, suppresses toxic fills via cancel-on-move thresholds, and hedges inventory on a liquid reference CEX only when hedge viability $\Gamma_h > 1$ captures net positive spread yield that systematically outperforms classical decoupled Avellaneda-Stoikov quoting.**

Economic failure modes are explicitly demarcated:
- If adverse selection consumes all spread capture ($\xi \geq 1$), quoting is unconditionally loss-making regardless of inventory or hedging heuristics.
- If market volatility is too low relative to CEX taker fees ($\Gamma_h \leq 1$), active hedging destroys capital through taker fee drag; the MM must switch to an unhedged spread-skewing and inventory-gated mode.
- If the correlation $\rho$ between the DEX perpetual and CEX hedge instrument falls below $\rho_{\min}$, hedging amplifies rather than reduces portfolio variance (basis risk trap).
- If the DEX funding rate persistently exceeds the CEX rate ($\Delta r_f > 0$), holding hedged long DEX / short CEX inventory incurs a negative carry that erodes liquidity-provision profits.

## Signal

The strategy operates across two interconnected control loops: high-frequency quoting on DEX-A and state-triggered inventory hedging on CEX-B.

### 1. High-Frequency Quoting Policy (DEX-A)

- **Reference State:** Mid-price $S_t$ on reference CEX-B (Brownian motion $\dd S_t = \sigma \dd W_t$). DEX-A mid-price $\tilde{S}_t = S_t + \beta_t$, where $\beta_t$ is an Ornstein-Uhlenbeck premium ($\dd \beta_t = -\kappa(\beta_t - \bar{\beta})\dd t + \sigma_\beta \dd W_t^\beta$).
- **Stationary Optimal Half-Spreads:** Under running inventory penalization $\phi(q) = \frac{1}{2}\eta q^2$ (Proposition 4.7):
  $$\delta^{b*}(q) = \frac{1}{k} + \alpha + \eta q + \frac{\eta}{2}$$
  $$\delta^{a*}(q) = \frac{1}{k} + \alpha - \eta q + \frac{\eta}{2}$$
  where:
  - $k$: order book depth / fill-rate sensitivity ($\lambda(\delta) = \Lambda e^{-k\delta}$).
  - $\alpha$: expected adverse selection cost per fill.
  - $\eta$: inventory risk-aversion penalty parameter ($\eta = \gamma \sigma^2 \tau_\eta$, calibrated to target inventory half-life).
  - $q$: current signed inventory (contracts).
- **Quote Placement:**
  $$P_t^b = \tilde{S}_t - \delta^{b*}(q)$$
  $$P_t^a = \tilde{S}_t + \delta^{a*}(q)$$
- **Total Quoted Spread:**
  $$s^*(q) = \delta^{b*}(q) + \delta^{a*}(q) = \frac{2}{k} + 2\alpha + \eta$$
  Total spread width is invariant to inventory $q$; inventory shifts the reservation mid-price $r_t = \tilde{S}_t - \eta q_t$ downward when long ($q > 0$) and upward when short ($q < 0$), discouraging adverse inventory accumulation.
- **Inventory Gating:** Hard absolute ceiling $\bar{q}$. If $q \geq \bar{q}$, cancel bid quote ($\delta^b = +\infty$). If $q \leq -\bar{q}$, cancel ask quote ($\delta^a = +\infty$).
- **Cancel-on-Move Threshold (Adverse Selection Filter):** Given cancel latency $\Delta t$, quotes are immediately canceled if reference price moves by more than $\theta^*$ (Proposition 3.7):
  $$\theta^* = \sigma \sqrt{\frac{1}{\rho_{\mathrm{cancel}}} \ln\left(\frac{k(\bar{\delta} - \alpha - c_\ell \sigma \sqrt{\Delta t})}{\rho_{\mathrm{cancel}}}\right)}$$
- **Online Sequential Bayesian Adverse Selection Estimation:**
  The informed trader fraction $\pi$ is updated after each fill $i$ with absolute price displacement $Z_i = |S_{\tau_i + h} - S_{\tau_i}|$ over horizon $h$:
  $$\hat{\pi}_n = \frac{a_0 + \sum_{i=1}^n \mathbf{1}\{Z_i > \theta_c\}}{a_0 + b_0 + n}$$
  where $\theta_c = \frac{1}{2}(\alpha_{\mathrm{info}} + c_\ell \sigma \sqrt{\Delta t})$. Adaptive adverse selection $\hat{\alpha}_n = \hat{\pi}_n \alpha_{\mathrm{info}} + (1 - \hat{\pi}_n) c_\ell \sigma \sqrt{\Delta t}$ replaces fixed $\alpha$ in the spread policy.

### 2. Cross-Exchange Hedging Policy (CEX-B)

- **Stationary Hedge Threshold:** Hedge on CEX-B only when absolute inventory exceeds (Corollary 7.3):
  $$q^*_\infty = \frac{\phi_t^{\mathrm{CEX}} \bar{S}}{\eta Q}$$
  When $|q_t| > q^*_\infty$, execute market hedge orders to reduce exposure to $q^{\mathrm{net}} = \mathrm{sign}(q_t) \cdot q^*_\infty$.
- **Funding-Adjusted Optimal Hedge Ratio:**
  $$\zeta_f^* = \left( 1 - \frac{n_h \phi_t^{\mathrm{CEX}} \bar{S}}{\gamma \sigma^2 \mathbb{E}[q_t^2] Q} - \frac{\mathbb{E}[r_f^{\mathrm{DEX}} - r_f^{\mathrm{CEX}}] \bar{S}}{\gamma \sigma^2 \mathbb{E}[q_t^2] Q \Delta_f} \sqrt{\frac{2 \mathbb{E}[q_t^2]}{\pi}} \right)^+$$
- **Hedge Re-evaluation Monitoring Interval:**
  $$\Delta \tau^* = \left(\frac{2 \phi_t^{\mathrm{CEX}} \bar{S}}{\gamma \sigma^2 Q \bar{\lambda}}\right)^{1/3}$$
- **Basis Risk Pre-Condition:** If hedging with an imperfect proxy instrument (correlation $\rho$, volatility $\sigma_h$), hedging is permitted only if:
  $$\rho > \rho_{\min} = \frac{n_h \phi_t^{\mathrm{CEX}} \bar{S}}{\gamma \sigma \sigma_h Q \mathbb{E}[q_t^2]}$$
- **Operational Entry/Exit Hysteresis:**
  Compute rolling adverse selection ratio $\xi_t = \hat{\alpha}_t / \bar{\delta}^*$. MM activates quoting when $\xi_t \leq \xi_{\mathrm{entry}}$ and pauses quoting when $\xi_t \geq \xi_{\mathrm{exit}}$, where the deadband satisfies:
  $$\Delta \xi = \xi_{\mathrm{exit}} - \xi_{\mathrm{entry}} \geq \sqrt{\frac{2(c_{\mathrm{entry}} + c_{\mathrm{exit}})}{\mathrm{APY}_0 (1 - \rho_\Sigma)}}$$

## Required data

- **Venues:** Primary quoting venue DEX-A (zero maker fee perpetual order book); reference venue CEX-B (high-liquidity reference perpetual or spot book, e.g., Binance).
- **Instruments:** Perpetual futures contracts (e.g., SOL-PERP, ETH-PERP, BTC-PERP, or liquid altcoins).
- **Timeframe & Sampling:** Sub-second tick-level order book depth (Level 2/3) and trade prints from DEX-A; millisecond top-of-book / trades from CEX-B.
- **Fields Required:**
  - DEX-A: Best bid/ask, order book depth profile (to calibrate fill sensitivity $k$), executed trade prices, side, and timestamps.
  - CEX-B: Reference mid-price $S_t$, executed trade prints, best ask/bid.
  - Funding Rates: Discrete periodic funding settlement rates $r_f^{\mathrm{DEX}}$ and $r_f^{\mathrm{CEX}}$, settlement countdown $\Delta_f$ (typically 8 hours or 1 hour).
  - Premium Process: Real-time basis / premium $\beta_t = \tilde{S}_t - S_t$.
- **Point-in-Time Constraints:** Reference price updates and cancel signals must be processed strictly before the subsequent DEX block/matching cycle. Look-ahead in cancel-on-move simulation is strictly forbidden.
- **Missing Data Handling:** If CEX reference feed drops or latency exceeds cancel threshold, instantly cancel all passive DEX quotes and enter idle state.

## Execution assumptions

### Source-reported (Theoretical Model)

- **Order Types:** Limit orders on DEX-A (earning zero maker fees, $\phi_m^{\mathrm{DEX}} = 0$); market/taker orders on CEX-B for inventory hedges (paying taker fees $\phi_t^{\mathrm{CEX}}$).
- **Fill Dynamics:** Double Poisson arrival with exponential depth penalty $\lambda(\delta) = \Lambda e^{-k\delta}$.
- **Order Size:** Constant order size $Q$ (normalized to 1 or fixed contracts in theoretical proofs; $Q = 10$ contracts in numerical simulation).
- **Capital & Leverage:** Deployed capital $K = K_{\mathrm{margin}} + K_{\mathrm{buffer}}$, leverage $\ell \in [3\times, 10\times]$.
- **Settlement:** Cash marked to market continuously; funding payments settled at discrete intervals $\Delta_f$.

### Research interpretation & Execution Realities

- **No Zero Latency:** Cancel latency $\Delta t > 0$ on DEX-A creates structural exposure to latency arbitrageurs. If CEX reference price moves faster than DEX cancel execution, quotes are sniped.
- **Block Time & RPC Jitter:** On decentralized order books (e.g., Hyperliquid L1, dYdX v4, Solana DEXs), deterministic continuous cancelation does not exist; cancelation is bounded by block production time ($50\text{--}200\text{ ms}$) and matching engine latency.
- **Partial Fills:** The theoretical assumption of constant fill size $Q$ must be relaxed in practice to support partial fills and queue priority degradation.
- **CEX Hedge Execution:** Market hedges on CEX-B suffer from taker fees $\phi_t^{\mathrm{CEX}} \approx 3\text{--}7.5\text{ bp}$ plus crossing slippage, requiring conservative calibration of $q^*_\infty$.

## Evidence

### Source-reported

All quantitative values below are reported directly by Minmin Zeng and Yi Liu (arXiv:2607.11888v1, Sections 5, 6, 7, 8, and Appendix D):

1. **Baseline Numerical Parameter Configuration (Table 4):**
   - Reference price $\bar{S} = \$20$, price volatility $\sigma = 0.30\%$ per minute, baseline fill rate $\Lambda = 30$ fills/hr.
   - Fill sensitivity $k = 200\ (1/\%)$, risk aversion $\gamma = 10^{-3}\ (1/\$)$, adverse selection $\alpha = 3\text{ bp}$.
   - DEX maker fee $\phi_m^{\mathrm{DEX}} = 0$, CEX taker fee $\phi_t^{\mathrm{CEX}} = 5\text{ bp}$.
   - Order size $Q = 10$ contracts, deployed capital $K = \$1,000$, leverage $\ell = 5\times$.
2. **Numerical Verification Across 15 Major Theoretical Results (Table 5):**
   - *Thm 4.3 (Inventory-Independent Total Spread):* Monte Carlo simulation (1,000 paths) confirms total spread $s^*$ is invariant to inventory with $<0.2\text{ bp}$ error.
   - *Thm 4.11 (Convergence Rate):* Grid search confirms $O(\tau_\eta^3)$ cubic PnL convergence rate of stationary penalization to finite-horizon optimal control.
   - *Thm 5.6 (High-APY Phase Boundary):* 5-parameter phase boundary verified via parameter sweep with $<3\%$ relative error.
   - *Thm D.1 (Master APY Factored Form):* Multiplicative Master APY formula verified via 3,000 Monte Carlo paths with $<1.5\%$ relative error.
   - *Prop 5.18 (Asymptotic Scaling Laws):* Linear scaling of APY with fill rate $\bar{\lambda}$ verified ($R^2 > 0.998$).
   - *Thm 5.21 (Drawdown Probability Bound):* Exponential tail bound $\mathbb{P}(\mathrm{MDD} > x) \leq e^{-\theta_{\mathrm{dd}} x}$ confirmed tight in the tail over 50,000 Monte Carlo paths.
   - *Thm 6.1 (Fee Floor Elimination):* Exact match on $2\phi_m$ structural APY advantage of zero-fee DEX over fee-bearing venues.
   - *Thm 7.5 & 7.11 (Optimal Hedge Ratio):* Interior optimal hedge ratio $\zeta^*$ and funding-adjusted ratio $\zeta_f^*$ verified with $<0.02$ absolute error and $<5\%$ relative error.
   - *Prop 7.7 (Hedge Check Interval):* Cube-root scaling $\Delta \tau^* \propto (\phi_t^{\mathrm{CEX}} / \gamma \sigma^2)^{1/3}$ confirmed numerically.
   - *Thm 7.16 (Basis Risk Threshold):* Critical correlation threshold $\rho_{\min}$ verified with $<0.03$ absolute error.
   - *Thm 6.10 (Entry/Exit Hysteresis):* Square-root hysteresis width $\Delta \xi \propto \sqrt{c_{\mathrm{entry}} + c_{\mathrm{exit}}}$ confirmed in non-stationary simulations.
   - *Thm 4.13 (Ergodic Inventory Distribution):* Gaussian inventory variance $\sigma_q^2 = \bar{\lambda}^* / (2\eta k)$ confirmed with $<4\%$ relative error.
   - *Thm 3.12 (Bayesian Convergence of $\pi$):* Sequential posterior concentrates at $O(n^{-1/2})$ rate; posterior converges from a misspecified prior $\mathrm{Beta}(5,5)$ ($\hat{\pi}_0 = 0.50$) to true $\pi = 0.15$ within $\sim 200$ fills ($\sim 1$ hour of trading).
   - *Thm 5.25 & Cor 5.26 (Multi-Pair Portfolio Allocation):* Diversification benefit saturates at $1/\sqrt{\bar{\rho}}$. For equi-correlation $\bar{\rho} = 0.30$, theoretical Sharpe improvement limit is $1/\sqrt{0.3} \approx 1.83$; 5 pairs achieve $\mathrm{SR}_5 / \mathrm{SR}_1 \approx 1.63$ ($\sim 85\%$ of theoretical maximum), while 10 pairs achieve $1.72$.
3. **Illustrative Return Scenarios (Example 5.28 & Section 8):**
   - Synthetic altcoin perpetual example ($K = \$1,000$, $5\times$ leverage, $\bar{\lambda} = 20/\text{hr} = 480/\text{day}$, $\bar{\delta} = 5\text{ bp}$, $\alpha = 2\text{ bp}$, $Q = 10$, $\bar{S} = \$20$): Net spread income per fill is $\$0.06$, yielding gross daily PnL of $\$28.80$ ($\$10,512/\text{year}$, gross $\mathrm{APY}_0 = 1,051\%$).
   - Accounting for realistic operational friction ($\rho_{\mathrm{inv}} \approx 0.15$, $\rho_{\mathrm{hedge}} \approx 0.10$), theoretical adjusted APY is $\sim 788\%$.
   - The authors explicitly state that under real-world slippage, execution failures, platform downtime, and adverse regime shifts, realistic sustainable annualized returns fall into the **50%–200% range**.

### Independently reproduced

not independently reproduced

### Negative evidence

- **Adverse Selection Insolvency:** When $\xi = \alpha / \bar{\delta}^* \geq 1$, expected PnL is negative across all trading regimes. Quoting on pairs with toxic taker flow ($\xi > 1$) cannot be rescued by risk aversion, inventory skewing, or leverage.
- **Hedging Destruction in Low Volatility:** When hedge viability $\Gamma_h \leq 1$, CEX taker fees ($\phi_t^{\mathrm{CEX}} \approx 5\text{ bp}$) exceed the variance reduction benefit. In this regime, cross-exchange hedging reduces APY and accelerates capital drawdown.
- **Basis Risk Failure:** When hedging with an imperfect proxy (e.g., hedging an altcoin perp with BTC/ETH perps), if correlation $\rho < \rho_{\min} \approx 0.60\text{--}0.70$, hedging actively *increases* total portfolio variance and ruins Sharpe ratio.
- **Funding Drag Asymmetry:** When the DEX funding rate trades persistently above the CEX rate ($r_f^{\mathrm{DEX}} > r_f^{\mathrm{CEX}}$), maintaining a hedged inventory position drains 20% to 40% of annualized yield through funding payments.
- **Universal Risk-Return Tradeoff:** The identity $\mathrm{APY} \times \mathrm{VaR}_{95\%}^{\mathrm{MDD}} = \mathrm{constant}$ proves that amplifying APY via higher leverage $\ell$ proportionally expands tail drawdown risk, invalidating claims of risk-free high APY.

## Falsification plan

1. **Zero-Fee Spread Floor Test:** Deploy passive quoting in a controlled paper simulation comparing a zero-maker-fee setting against a 2 bp maker fee setting. **Falsification threshold:** If realized net edge does not increase by exactly the fee difference $2\phi_m$ (holding fill rates and adverse selection equal), reject the fee floor elimination theorem.
2. **Total Spread Inventory-Invariance Test:** Track total bid-ask spread $s^*_t = \delta^{b*}_t + \delta^{a*}_t$ as inventory $q_t$ fluctuates from $-\bar{q}$ to $+\bar{q}$. **Falsification threshold:** If the total spread width varies by more than $0.5\text{ bp}$ as a function of inventory $q$, reject the theoretical optimal spread derivation.
3. **Adverse Selection Cutoff ($\xi \geq 1$):** Identify tokens/regimes where measured adverse selection $\alpha$ exceeds half-spread $\bar{\delta}^*$. **Falsification threshold:** If an agent quoting with $\xi \geq 1.05$ achieves statistically significant positive cumulative PnL over $>5,000$ fills, reject the necessary condition for profitability (Theorem 5.5).
4. **Hedge Viability Regime Test ($\Gamma_h$):** In an environment with low volatility ($\sigma < 1.5\text{ bp}/\sqrt{\text{s}}$) and standard CEX taker fees ($\phi_t^{\mathrm{CEX}} \geq 5\text{ bp}$), compare an active hedging policy against a no-hedge inventory-gated policy. **Falsification threshold:** If active cross-exchange hedging achieves higher net Sharpe ratio than the no-hedge policy when $\Gamma_h \leq 1$, reject the hedge regime classification (Definition 7.13).
5. **Basis Risk Degradation Test:** For altcoin perpetuals, execute cross-hedges using reference instruments with varying empirical correlation $\rho$. **Falsification threshold:** If hedging with an instrument having $\rho < \rho_{\min}$ reduces portfolio variance compared to unhedged inventory, reject Theorem 7.16.
6. **Ergodic Inventory Distribution Test:** Run the stationary policy over $>50,000$ simulated fills with inventory penalty $\eta$. **Falsification threshold:** If realized inventory distribution deviates from Gaussian normality (Jarque-Bera $p < 0.01$) or if stationary variance $\sigma_q^2$ differs from $\bar{\lambda}^* / (2\eta k)$ by $>10\%$, reject Theorem 4.13.
7. **Bayesian Convergence Rate Test:** Inject known synthetic informed order flow fractions $\pi \in \{0.05, 0.15, 0.30\}$. **Falsification threshold:** If the posterior estimator $\hat{\pi}_n$ fails to concentrate within a $95\%$ credible interval of width $\leq 3.92\sqrt{\pi(1-\pi)/n}$ after $n = 500$ fills, reject Theorem 3.12.

## Crypto portability

- **Portability:** `direct` for cryptocurrency perpetual futures markets.
- **Structural Alignment:** The framework is natively formulated for crypto perpetual contracts, incorporating 24/7 continuous trading, 8-hour/1-hour funding rate settlement cycles, decentralized order book venues with zero maker fees (e.g., Hyperliquid L1, dYdX v4, Aevo), and centralized reference exchanges (e.g., Binance, OKX).
- **Crypto-Specific Execution Hazards:**
  1. *L1 Block Latency & MEV:* Decentralized order books execute on discrete block intervals. Front-running and latency arbitrage by toxic flow exploiting CEX-DEX price feeds can severely inflate $\alpha$ beyond theoretical bounds.
  2. *Liquidation Spills:* Crypto market flash crashes trigger auto-deleveraging (ADL) and cascading liquidations, violating the zero-drift arithmetic Brownian motion assumption ($\mu = 0$) and causing extreme inventory gating breaches ($|q| > \bar{q}$).
  3. *Exchange Counterparty & Margin Segregation:* Cross-exchange hedging requires maintaining collateral across both DEX and CEX venues, introducing margin fragmentation and liquidation risk on the hedging leg during high-volatility spikes.

## Limitations

- **Synthetic Simulation Baseline:** All numerical results in the primary source are derived from Monte Carlo simulations with synthetic parameters; no live exchange order fills or tick-level empirical exchange datasets were tested.
- **Stylized Fill Dynamics:** The assumption of double Poisson fill arrivals with exponential spread decay $\Lambda e^{-k\delta}$ ignores order book queue priority, cancellation cascades, and size-dependent market depth.
- **Deterministic Order Size:** The model assumes constant order size $Q$, failing to capture partial fills and variable taker order sizes prevalent in crypto order books.
- **Uncorrelated Funding Rate Simplification:** The paper models funding rate $r_f(t)$ and premium $\beta_t$ as independent Ornstein-Uhlenbeck diffusions for mathematical tractability, whereas empirical crypto markets exhibit strong positive correlation $\mathrm{Corr}(r_f, \beta) > 0$ during bull runs and negative during bear crashes.
- **Policy Risk:** Zero-maker-fee structures are subject to sudden platform governance or fee tier revisions; introducing even a $1\text{--}2\text{ bp}$ maker fee materially contracts the profitable phase space.
- **Not Independently Reproduced.**

## Implementation status

No implementation has been performed in PyBroker, NautilusTrader, paper trading, testnet, or live trading environments. This record captures the theoretical research model and numerical validation only.

## Adoption boundary

- `status: research-only`
- `implementation_status: not-implemented`
- `adoption: not-approved`
- `approval_scope: research-only`

This document is an upstream research capture. It does not authorize capital deployment, live liquidity provision, strategy registration, or production trading on any exchange.

## Related Wiki records

- `[[quant/signal-to-executable-pnl-costs-2026-08-28]]` — Framework for bridging theoretical spread signals to net executable PnL under venue frictions.
- `[[quant/phase10-universe-lifecycle-survivorship-2026-08-28]]` — Venue lifecycle, liquidity stability, and delisting considerations.
- `[[funding-aware-market-making-perpetual-dex-2026-08-31]]` — Single-venue stochastic funding HJB market making formulation (Le 2026).
- `[[market-making-axiomatic-unified-inventory-quoting-spread-decomposition-2026-09-02]]` — Axiomatic spread decomposition models.
- `[[market-making-latent-fad-stochastic-control-hjb-2026-09-02]]` — Latent flow-adjusted drift HJB control.

## Sources

1. Minmin Zeng and Yi Liu (2026), *Optimal Adaptive Market Making: A Theoretical Framework for High-Yield Liquidity Provision in Perpetual Futures Markets*, arXiv preprint arXiv:2607.11888v1 [cs.AI, q-fin.TR, q-fin.PM], submitted 16 Jul 2026. DOI: `10.48550/arXiv.2607.11888`. Stable abstract: https://arxiv.org/abs/2607.11888. Full text: https://arxiv.org/html/2607.11888v1.
2. Marco Avellaneda and Sasha Stoikov (2008), *High-frequency trading in a limit order book*, Quantitative Finance, 8(3), 217–224. DOI: `10.1080/14697680701698146`.
3. Olivier Guéant, Charles-Albert Lehalle, and Joaquin Fernandez-Tapia (2012), *Dealing with the inventory risk: a solution to the market making problem*, Mathematics and Financial Economics, 6(4), 259–277. DOI: `10.1007/s11579-012-0087-0`.
4. Lawrence R. Glosten and Paul R. Milgrom (1985), *Bid, ask and transaction prices in a specialist market with heterogeneously informed traders*, Journal of Financial Economics, 14(1), 71–100. DOI: `10.1016/0304-405X(85)90044-3`.
5. Álvaro Cartea, Sebastian Jaimungal, and Jason Penalva (2015), *Algorithmic and High-Frequency Trading*, Cambridge University Press. DOI: `10.1137/130946256`.
