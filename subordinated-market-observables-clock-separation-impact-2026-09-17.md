---
schema: strategy-research-record-v1
title: "Subordinated Market Observables: Clock Separation for Order-Flow Memory and Square-Root Impact"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - price-impact
  - order-flow-memory
  - reaction-diffusion
  - subordination
  - inverse-subordinator
  - square-root-law
  - lillo-mike-farmer
  - anomalous-diffusion
status: research-only
confidence: high
source_as_of: 2026-09-12
sources:
  - https://arxiv.org/abs/2609.13715
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Subordinated Market Observables: Clock Separation for Order-Flow Memory and Square-Root Impact

## Provenance

- **Primary Source:** Christopher Angstmann (School of Mathematics and Statistics, UNSW Sydney, Australia, `c.angstmann@unsw.edu.au`) and Tim Gebbie (Department of Statistical Sciences, University of Cape Town, South Africa, `tim.gebbie@uct.ac.za`), *"Event-Time Order-Flow Memory, Operational-Time Impact, and Subordinated Market Observables"*, arXiv preprint `arXiv:2609.13715v1 [q-fin.TR, math-ph, math.MP, physics.soc-ph, q-fin.ST]`, submitted September 12, 2026.
  - Journal Status: Accepted for publication in *Journal of Statistical Mechanics: Theory and Experiment* (JSTAT) (`source-reported`).
  - Stable Abstract URL: https://arxiv.org/abs/2609.13715
  - Full-Text HTML Source: https://arxiv.org/html/2609.13715v1
  - Full-Text PDF Source: https://arxiv.org/pdf/2609.13715v1
  - Canonical DOI: [10.48550/arXiv.2609.13715](https://doi.org/10.48550/arXiv.2609.13715)
- **Direct Primary-Source Verification:** The complete preprint manuscript, Sections 1–7, Equations (1)–(19), and References [1]–[25] were directly inspected via the full-text HTML interface (`https://arxiv.org/html/2609.13715v1`). All mathematical statements, lattice update equations, discrete imbalance cancellations, Abel-kernel Volterra integral solutions, and inverse subordinator scaling relations cited in this record trace directly to `arXiv:2609.13715v1`. No search-result snippets, secondary reviews, or synthetic aggregators were used to formulate strategy mechanics or claims.
- **Repository Deduplication Audit:** Pre-write search across all Markdown records in `alpha-strategy-research` confirmed zero existing records citing `arXiv:2609.13715`, Christopher Angstmann, or Tim Gebbie. Adjacent microstructure and execution records in the repository investigate distinct mechanisms:
  - `diffusive-price-dynamics-square-root-impact-lmf-levy-walk-2026-09-17.md` (Sato, Fujiwara, Kanazawa 2026, arXiv:2608.00988) investigates the diffusive price-dynamics paradox using a nonlinear generalization of the LMF model mapped onto an event-indexed continuous-time random walk / Lévy walk; it treats regularizations as event-indexed source properties and does not decouple operational reaction fronts from calendar subordination.
  - `portfolio-representation-switching-frictions-order-flow-long-memory-2026-09-17.md` (Rodríguez Domínguez 2026, arXiv:2609.02525) explores costly switches between discrete portfolio representations as an upstream economic source of order-flow memory, without deriving reaction-diffusion front transport or subordination kernels.
  - `duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11.md` (Jebali 2026, arXiv:2609.07989) develops online changepoint detection for duration and arrival-rate distributions, but does not embed them into a latent order-book reaction-diffusion model or derive calendar-time impact scaling laws.
  - `fifo-queue-partial-identification-l2-execution-sensitivity-2026-09-16.md` (Danait, Zamora, Boier 2026, arXiv:2609.13597) establishes partial identification bounds for FIFO fill outcomes under level-2 snapshot intervals, without formulating operational-time continuous limits.
  - `model-free-passive-execution-order-level-shadowing-ppov-2026-09-17.md` (Maciejewski 2026, arXiv:2609.18019) formulates model-free passive order-level shadowing without explicit impact kernels.

## Economic mechanism

### Source-reported

Angstmann & Gebbie establish that two foundational empirical regularities in quantitative market microstructure are defined on fundamentally different clocks and cannot be treated as functions of a single common time variable without implicit, distortive subordination:

1. **Trade-Sign Long Memory is an Event-Time Regularity ($m$):**
   The persistent autocorrelation of aggressive child-order signs ($\epsilon_m \in \{-1, +1\}$) is native to the **event clock** ($m \in \{1, 2, \dots\}$). In the sequential hidden-order order-splitting framework of Lillo, Mike, and Farmer (LMF, 2005), institutional investors break large parent meta-orders into sequences of child orders. If meta-order lengths $L$ follow a Pareto distribution $p_L(\ell) \sim c_L \ell^{-(\alpha+1)}$ with $\alpha \in (1, 2)$, a randomly sampled child order encounters the length-biased distribution $\pi_L(\ell) = \ell p_L(\ell) / \langle L \rangle$. The event-time sign autocorrelation is exactly:
   $$C_m(k) := \mathbb{E}[\epsilon_m \epsilon_{m+k}] = \sum_{\ell=k+1}^\infty \frac{\ell - k}{\langle L \rangle} p_L(\ell) \sim c_C k^{-(\alpha-1)} = c_C k^{-\gamma}$$
   with $\gamma = \alpha - 1 \in (0, 1)$. This mechanism is purely renewal-theoretic and depends strictly on event ordering and meta-order length distributions, entirely independent of price dynamics or execution clocks.

2. **The Square-Root Law of Market Impact is an Operational-Time Regularity ($u$):**
   The concave price impact of meta-orders is native to the **operational continuum clock** ($u = m \Delta u$). Starting from a symmetric discrete-time random-walk (DTRW) bid/ask lattice model with order survival $\theta_j^{m,m-1} = e^{-\nu \tau_m}$, cancellation rate $\nu$, reaction rate $\kappa$, diffusion limit $D = \lim_{\Delta x, \tau_m \to 0} (r/2)\Delta x^2 / \tau_m$, and signed forcing $\mathcal{M}_{j,m} = M_{j,m}^B - M_{j,m}^A$, the discrete imbalance field $\phi_j^m = \rho_{B,j}^m - \rho_{A,j}^m$ satisfies:
   $$\phi_j^m - \phi_j^{m-1} = D \frac{\tau_m}{\Delta x^2} \left[\phi_{j+1}^m - 2\phi_j^m + \phi_{j-1}^m\right] - \nu \tau_m \phi_j^m + s_{j,m} + \mathcal{M}_{j,m}$$
   Crucially, the nonlinear symmetric matching term $-\kappa \rho_{B,j}^m \rho_{A,j}^m$ cancels *exactly* upon subtraction, yielding a closed linear recursion for the imbalance field conditional on the realized waiting times $\tau_m$.
   In the operational continuum limit $u$, the imbalance field perturbation $\Psi(x,u) = \Phi(x,u) - \Phi^*(x)$ satisfies:
   $$\partial_u \Psi(x,u) = D \partial_{xx} \Psi(x,u) - \nu \Psi(x,u) - m_u \delta(x - y(u))$$
   Evaluating this perturbation at the moving reaction front $y(u)$ (defined by $\Phi(y(u),u) = 0$) in the locally linear latent-order-book regime ($\Phi^*(x) \approx -\mathcal{L}_u(x - y_0)$ with local liquidity slope $\mathcal{L}_u = -\partial_x \Phi^*(y_0) > 0$) yields the Abel-kernel Volterra integral equation:
   $$\mathcal{L}_u (y(u) - y_0) = \int_0^u ds \, \frac{e^{-\nu(u-s)}}{\sqrt{4\pi D (u-s)}} m_e(s) \exp\left( -\frac{(y(u) - y(s))^2}{4D(u-s)} \right)$$
   For constant execution rate $m_e(s) = m_0 \mathbf{1}_{[0,U]}(s)$ in the weak-cancellation, small-displacement regime, this reduces directly to the classic operational-time square-root law:
   $$y(u) - y_0 \approx \frac{2 m_0}{\mathcal{L}_u \sqrt{\pi D}} \sqrt{u}$$
   At completion $Q_U = m_0 U$, peak impact is strictly proportional to $\sqrt{Q_U}$ at fixed operational participation rate. The square-root law is generated entirely by diffusive transport memory on the operational clock, not by order-splitting sign persistence.

3. **Calendar-Time Observables Arise via Subordination ($t$):**
   Calendar time ($t$) is generated by the cumulative waiting-time process $T_m = \sum_{k=1}^m \tau_k$ with inverse event counter $N_t = \max \{m : T_m \le t\}$ and continuous inverse subordinator $E_t = \inf \{u \ge 0 : T(u) > t\}$.
   - The observed calendar-time sign process is $\epsilon(t) = \epsilon_{N_t}$, with correlation $C_t(t_1, t_2) = \mathbb{E}[C_m(N_{t_2} - N_{t_1})]$.
   - The observed calendar-time price front is $Y_t = y(E_t) \approx y_0 + \frac{2 m_0}{\mathcal{L}_u \sqrt{\pi D}} \sqrt{E_t}$.
   - **Finite-mean waiting times:** If $\mathbb{E}[\tau] = \bar{\tau} < \infty$, the inverse subordinator scales linearly ($E_t \sim t / \bar{\tau}$), recovering the standard calendar-time square-root law up to deterministic activity rescaling:
     $$Y_t - y_0 \propto \sqrt{\frac{t}{\bar{\tau}}}$$
   - **Heavy-tailed waiting times:** If inter-event durations follow a heavy-tailed stable distribution with index $\beta \in (0, 1)$, the inverse subordinator scales as $E_t \sim t^\beta$, producing an anomalous calendar-time impact curve:
     $$Y_t - y_0 \propto t^{\beta / 2}$$
   - **Tempered stable clocks:** At intraday timescales where power-law bursts dominate, impact follows $t^{\beta / 2}$; at longer horizons where exponential tempering restores finite mean, impact crosses over to the standard $t^{1/2}$ scaling.

4. **Resolution of the Memory-Return Paradox:**
   Long-memory order flow does not produce superdiffusive or long-memory price returns because the event-time forcing is filtered through two distinct layers:
   - First filter: from event-time forcing to operational front motion via diffusive replenishment, cancellation, and local liquidity adaptation ($\mathcal{L}_u, D, \nu$);
   - Second filter: from operational front observables to calendar time via stochastic subordination ($E_t$).

### Research interpretation

This clock-separation framework provides a rigorous, falsifiable foundation for **operational execution pacing and order-flow alpha conditioning**:

- **The Subordination Distortion in Algorithmic Execution:** Conventional execution models (Almgren-Chriss, Obizhaeva-Wang, Gatheral) formulate price impact as a direct function of calendar time $t$ or volume share $v$. When market activity shifts into heavy-tailed burst regimes ($\beta < 1$, common during high-volatility news or cascading liquidations), calendar-time impact compresses from $t^{1/2}$ to $t^{\beta/2}$. A static calendar-time execution algorithm (e.g., rigid TWAP) assumes impact accumulates as $t^{1/2}$, misestimating market resistance and overpaying for execution during quiet inter-burst periods while underutilizing high-liquidity burst periods.
- **Dynamic Operational-Pacing Alpha:** By monitoring the instantaneous inverse subordinator rate $dE_t / dt$ (estimated via empirical trade-arrival intensity and duration scaling), an execution agent can pace meta-orders in operational time $u$ rather than physical clock time $t$. Pacing meta-orders at constant operational participation rate preserves the true minimal-impact trajectory $I(u) \propto \sqrt{u}$, reducing total slippage relative to calendar-benchmarked competitors.
- **De-aliased Order-Flow Imbalance Signals:** Signal researchers who construct order-flow imbalance (OFI) or cumulative volume delta (CVD) over fixed calendar intervals (e.g., 1-second or 1-minute bars) induce artificial time-aggregation bias: quiet periods aggregate few renewal events (over-weighting idiosyncratic noise), while burst periods compress dozens of meta-orders into a single bar (destroying the true LMF power-law memory structure). Conditioning predictive signals on the native event clock ($m$) preserves the true renewal exponent $\gamma = \alpha - 1$.

## Signal

The strategy framework comprises two distinct operational components: an **Operational-Pacing Execution Signal** and an **Event-Clock Order-Flow Momentum Signal**.

### 1. Operational-Pacing Execution Engine

- **Event Clock Tracking (`source-reported`):**
  For each incoming trade event $m$, record timestamp $t_m \in \mathbb{R}^+$, signed volume $q_m \in \mathbb{R}$, and aggressor direction $\epsilon_m \in \{-1, +1\}$.
  Compute inter-event durations:
  $$\tau_m = t_m - t_{m-1}$$
- **Rolling Tail Index Estimation (`research-proposed`):**
  Over a rolling event window of $W_\tau = 1,000$ consecutive trade arrivals (`research-proposed`), estimate the local Pareto/stable tail index $\hat{\beta}_m \in (0, 1]$ of the duration distribution using the Hill estimator on durations exceeding the 75th percentile threshold $\tau_{\text{thresh}}$ (`research-proposed`):
  $$\hat{\beta}_m = \left( \frac{1}{K_\tau} \sum_{k=1}^{K_\tau} \ln\left( \frac{\tau_{(m-k+1)}}{\tau_{\text{thresh}}} \right) \right)^{-1}$$
- **Subordination Regime Gating:**
  - **Homogeneous Regime ($\hat{\beta}_m \ge 0.85$, `research-defined falsification threshold`):** The market operates under finite-mean waiting times. Calendar time approximates operational time ($E_t \propto t$). Execute meta-orders using standard square-root participation pacing $m_0 \propto \sqrt{\Delta t}$.
  - **Subordinated Burst Regime ($\hat{\beta}_m < 0.70$, `research-defined falsification threshold`):** The market operates under heavy-tailed subordination. Calendar-time impact scales as $t^{\hat{\beta}_m / 2}$. Compress execution into event bursts and withhold child orders during long inter-event pauses.
  - **Transition Hysteresis Band ($0.70 \le \hat{\beta}_m < 0.85$, `research-proposed`):** Maintain prior regime state to prevent thrashing.

### 2. Event-Clock Order-Flow Momentum Signal

- **Signal Formation Timestamp:** Evaluated strictly at the confirmation of trade event $m$ (`source-reported`).
- **Lookback Window:** Fixed event-count window of $K_{\text{event}} = 100$ trades (`research-proposed`), completely invariant to elapsed calendar time.
- **Event-Time Imbalance Metric (`research-proposed`):**
  $$\text{OFI}_m^{\text{event}} = \frac{\sum_{k=0}^{K_{\text{event}}-1} \epsilon_{m-k} |q_{m-k}|}{\sum_{k=0}^{K_{\text{event}}-1} |q_{m-k}|}$$
- **Entry Logic (`research-proposed`):**
  - **Long Entry:** $\text{OFI}_m^{\text{event}} > +0.35$ (`research-defined falsification threshold`) AND $\hat{\beta}_m < 0.70$ (confirming active burst subordination) AND mid-price $P_m > \text{EMA}_{500}^{\text{event}}(P)$ (`research-proposed` trend regime filter).
  - **Short Entry:** $\text{OFI}_m^{\text{event}} < -0.35$ (`research-defined falsification threshold`) AND $\hat{\beta}_m < 0.70$ AND mid-price $P_m < \text{EMA}_{500}^{\text{event}}(P)$.
- **Exit Logic (`research-proposed`):**
  - **Event-Horizon Exit:** Close position after exactly $H_{\text{event}} = 250$ trade events (`research-proposed`) following entry.
  - **Sign Reversal Exit:** Close immediately if $\text{OFI}_m^{\text{event}}$ flips sign with magnitude $> 0.20$ (`research-proposed`).
  - **Calendar Timeout Emergency Stop:** Close unconditionally if $t - t_{\text{entry}} > 1,800\text{ seconds}$ (30 minutes, `research-proposed`) to guard against market freezes or extreme liquidity dry-ups.
  - **Adverse Price Stop:** 1.5 $\times \text{ATR}_{100}^{\text{event}}$ (`research-proposed`).

## Required data

- **Instrument / Universe:** Liquid centralized exchange perpetual futures contracts (e.g., BTC-USDT, ETH-USDT, SOL-USDT on Binance / Bybit) or highly active equity index futures (e.g., CME E-mini S&P 500 `ES`, Nasdaq `NQ`) (`research-proposed`).
- **Data Modality & Granularity:**
  - Full tick-by-tick public trade prints (`aggTrades` or raw execution stream) including:
    - Nanosecond or microsecond exchange matching-engine timestamp $t_m$;
    - Transaction price $P_m$;
    - Executed volume / quantity $q_m$;
    - Buyer/seller maker indicator (identifying trade sign $\epsilon_m \in \{-1, +1\}$ without ambiguity).
  - Top-of-book (Level-1 / BBO) quotes synchronized to each trade event to evaluate the empirical mid-price front $x_m^* \approx (P_{B,m} + P_{A,m})/2$ and spread.
  - High-frequency Level-2 depth snapshots (minimum 10 levels at 100 ms intervals) to calibrate the local stationary liquidity slope $\hat{\mathcal{L}}_u = -\partial_x \Phi^*(y_0)$ and estimate local diffusion $D$ (`research-proposed`).
- **Point-in-Time Integrity:**
  - Duration calculations $\tau_m = t_m - t_{m-1}$ and rolling Hill estimators $\hat{\beta}_m$ must use strictly historical event prints up to index $m$.
  - Absolutely zero forward-looking duration sampling or post-hoc event count normalization.

## Execution assumptions

- **Order Type:** Limit orders pegged to the near-touch (best bid for buys, best ask for sells) when executing passive market-making or pacing; aggressive marketable IOC/FOK orders when triggering momentum signals (`research-proposed`).
- **Execution Timing:** Next-event execution. Signal formed on trade print $m$; orders submitted to matching engine with assumed round-trip network/gateway latency of $\delta_{\text{lat}} = 10\text{ ms}$ (`research-proposed`).
- **Fill Model:** Price-time priority FIFO queue model. No instantaneous fill assumption; orders must cross spread or wait for passive fill matching.
- **Transaction Costs & Slippage (`research-proposed`):**
  - Taker fee: 4.0 bps (0.040%);
  - Maker fee: 1.5 bps (0.015%);
  - Impact model: Subordinated operational-time square-root impact $I(\Delta t) = \frac{2 m_0}{\mathcal{L}_u \sqrt{\pi D}} \sqrt{E_{\Delta t}}$ where $E_{\Delta t} \sim (\Delta t / \bar{\tau})^{\hat{\beta}}$.
- **Borrow & Funding:** Spot borrow / perpetual funding rate modeled explicitly. Positions held across 8-hour funding intervals accrue standard funding debits.

## Evidence

### Source-reported

All analytical derivations and structural theorems below are reported directly by Christopher Angstmann and Tim Gebbie (`arXiv:2609.13715v1`, September 2026):

1. **Exact Imbalance Reduction (Section 2, Eq. 7):**
   Subtracting the ask-side discrete random-walk equation from the bid-side equation cancels the nonlinear annihilation reaction term $-\kappa \rho_B \rho_A$ identically, yielding the exact linear closed-form recursion for the imbalance field $\phi_j^m$:
   $$\phi_j^m - \phi_j^{m-1} = D \frac{\tau_m}{\Delta x^2} \left[\phi_{j+1}^m - 2\phi_j^m + \phi_{j-1}^m\right] - \nu \tau_m \phi_j^m + s_{j,m} + \mathcal{M}_{j,m}$$
   This cancellation holds for arbitrary non-negative waiting-time sequences $\{\tau_m\}$ and does not depend on the underlying probability law of the event clock.

2. **Abel-Kernel Volterra Impact Derivation (Section 3, Eqs. 10–12):**
   In the operational continuum limit $u = m \Delta u$, evaluating the perturbation at the moving interface $y(u)$ under locally linear background $\Phi^*(x) \approx -\mathcal{L}_u(x - y_0)$ yields the closed Volterra integral equation of the second kind. In the weak cancellation limit ($\nu \to 0$), the kernel is exactly the Abel kernel $(u - s)^{-1/2}$, proving that the operational-time front trajectory satisfies:
   $$y(u) - y_0 \approx \frac{2 m_0}{\mathcal{L}_u \sqrt{\pi D}} \sqrt{u}$$
   confirming that the square-root law of market impact is generated by diffusive transport on the operational clock.

3. **Exact Renewal Trade-Sign Memory (Section 4, Eqs. 13–15):**
   Under sequential meta-order splitting with Pareto parent sizes $p_L(\ell) \sim c_L \ell^{-(\alpha+1)}$, the event-time autocorrelation satisfies the Lillo-Mike-Farmer relation $C_m(k) \propto k^{-(\alpha-1)}$ strictly as an event-time renewal law.

4. **Subordinated Impact Scaling (Section 5, Eqs. 18–19):**
   Subordinating the operational front motion to calendar time via the inverse subordinator $E_t = \inf \{u \ge 0 : T(u) > t\}$ proves that:
   - For finite-mean waiting times ($\mathbb{E}[\tau] < \infty$), $E_t \propto t$ and the standard clock-time square-root law $Y_t - y_0 \propto \sqrt{t}$ holds.
   - For heavy-tailed waiting times with stable index $\beta \in (0, 1)$, typical scaling is $E_t \sim t^\beta$, and observed calendar-time impact scales anomalously as $Y_t - y_0 \propto t^{\beta / 2}$.
   - Fractional impact behavior enters exclusively through the event-to-calendar clock projection, not through an altered operational-time impact kernel.

5. **Empirical Performance Figures:**
   The primary paper is a rigorous mathematical physics and statistical mechanics work accepted at *JSTAT*. It reports analytical theorems and exact structural solutions; it does **not** assert empirical backtest Sharpe ratios, win rates, annualized returns, or maximum drawdowns on specific historical asset databases. No empirical quantitative performance statistics are invented here.

### Independently reproduced

`Not independently reproduced.`

No internal backtest or high-frequency simulation of the subordinated reaction-diffusion model has been conducted in this research stack.

### Negative evidence

- **Breakdown under Strong Nonlinear Order-Book Curvature:** The analytic derivation of the square-root law requires the locally linear latent-order-book approximation ($\Phi^*(x) \approx -\mathcal{L}_u(x - y_0)$ near the reaction front). In markets with thin books, large bid-ask spreads, or convex liquidity profiles (e.g., highly illiquid altcoins or exotic derivatives), local linearity fails, and the Abel-kernel reduction no longer yields exact $\sqrt{u}$ scaling (`source-reported`).
- **Coupled / State-Dependent Event Clocks:** The subordination formulation assumes an exogenous waiting-time process $T_m$ independent of front displacement $y(u)$. In real financial markets, extreme price moves trigger endogenous self-exciting Hawkes feedback (stop-loss runs, liquidation spirals), coupling $E_t$ directly to $y(u)$. Under strong state dependence, the clean factorization between operational transport and clock projection degrades (`source-reported`).
- **No Direct Profitability Guarantee:** As emphasized by the authors, separating the clocks resolves the theoretical paradox between long-memory order flow and short-memory returns, but does not imply that raw order-flow memory generates unconstrained arbitrage profits after realistic trading frictions (`source-reported`).

## Falsification plan

To empirically test and falsify the subordinated clock-separation hypothesis:

1. **Test 1: Event-Time vs. Calendar-Time Autocorrelation Stability:**
   - *Data:* 6 months of tick-level trade prints for BTC-USDT perpetual futures on Binance.
   - *Procedure:* Compute sample autocorrelation $C(k)$ of trade signs $\epsilon$ across: (a) native event index $k \in [1, 10^4]$; (b) calendar-time 1-second sampled signs; (c) calendar-time 10-second sampled signs.
   - *Decision Rule (`research-defined falsification threshold`):* If the estimated decay exponent $\hat{\gamma}$ on the event clock remains stable within $\pm 0.05$ across high-volume and low-volume sub-periods while calendar-time decay exponents fluctuate by $> 0.25$ between active and quiet sessions, the clock-separation thesis is supported. If event-time autocorrelation exhibits instability comparable to calendar-time autocorrelation, the pure event-time renewal thesis is falsified.
2. **Test 2: Anomalous Calendar Impact Scaling vs. Waiting-Time Exponent:**
   - *Data:* High-frequency meta-order execution dataset partitioned into two subsets: Regime A ($\hat{\beta} > 0.85$, Poisson-like arrivals) and Regime B ($\hat{\beta} < 0.65$, heavy-tailed burst arrivals).
   - *Procedure:* Fit empirical impact curves $I(t) \propto t^\eta$ over calendar execution time $t \in [1, 300]\text{ seconds}$.
   - *Decision Rule (`research-defined falsification threshold`):* The primary theory predicts $\eta_A \approx 0.50$ and $\eta_B \approx \hat{\beta}/2 \le 0.325$. If the estimated exponent in Regime B satisfies $|\eta_B - 0.50| < |\eta_B - \hat{\beta}/2|$, the hypothesis that calendar impact anomaly is driven by inverse subordinator scaling is falsified.
3. **Test 3: Operational-Pacing Implementation Shortfall Reduction:**
   - *Procedure:* Backtest a meta-order execution algorithm that paces child orders uniformly in operational time $u$ (allocating size proportional to estimated $d\hat{E}_t / dt$) against standard calendar TWAP and volume-curve VWAP over 1,000 synthetic institutional execution blocks.
   - *Decision Rule (`research-defined falsification threshold`):* If operational pacing fails to achieve a statistically significant ($t > 2.0$, $p < 0.05$) reduction in implementation shortfall of at least $1.5\text{ bps}$ after full taker fees and adverse selection, reject the operational-pacing execution advantage.

## Crypto portability

- **Portability Classification:** `adapted`.
- **Portability Justification & Adaptation Requirements:**
  - The primary paper establishes the theoretical framework for continuous double auction limit order books in abstract log-price space without crypto-specific empirical estimation (`source-reported`).
  - Applying this framework to cryptocurrency markets represents a research adaptation (`research interpretation`):
    - **Burstiness & Heavy Tails:** Crypto markets exhibit extreme trade-arrival burstiness driven by programmatic liquidation engines, algorithmic market makers, and cross-DEX/CEX arbitrage bots. Consequently, the empirical duration exponent $\beta$ is frequently deep in the anomalous regime ($\beta < 0.70$) during volatility events, making subordination effects far more pronounced than in traditional equities.
    - **Continuous 24/7 Clock:** Unlike traditional equity markets with overnight closures and opening/closing crosses that disrupt renewal memory, crypto markets operate 24/7. This allows long-memory event-time processes ($C_m(k) \propto k^{-\gamma}$) to persist unbroken over much longer event horizons.
    - **Perpetual Funding Dynamics:** In crypto perpetuals, regular 8-hour funding intervals create exogenous predictable spikes in trade arrival intensity, temporarily shifting the waiting-time law from heavy-tailed to high-rate Poisson. Operational pacing models must explicitly incorporate funding boundary conditions.
    - **Venue Fragmentation:** Crypto liquidity is fragmented across multiple non-fungible centralized and decentralized venues. Operational time $u$ advances at different rates on Binance vs. Bybit vs. Coinbase for the same underlying asset, necessitating venue-specific subordinator tracking.

## Limitations

- **Purely Theoretical Microstructure Derivation:** The cited primary source is a theoretical mathematical physics paper. It does not provide empirical backtest returns, live execution logs, or Sharpe ratios. Any trading application is an adapted research hypothesis.
- **Unverified Parameter Calibration:** Estimating the local liquidity slope $\mathcal{L}_u$ and the order-book diffusion parameter $D$ in real time requires continuous fitting of high-frequency order-book profiles, which is sensitive to market-maker quote cancellations and quote stuffing.
- **Underspecified Optimal Execution Schedule:** While the paper derives the forward impact for constant operational-rate forcing $m_0 \mathbf{1}_{[0,U]}(u)$, it does not solve the stochastic optimal control problem for an impact-minimizing trajectory under state-dependent $\beta(t)$.
- **Exogenous Subordination Assumption:** The assumption of an independent event clock is an abstraction; during crash regimes, price displacement and order arrivals are strongly coupled.

## Implementation status

`not-implemented`.

No software implementation, backtest script, or execution handler has been written or deployed in `nautilus-quant-system`, PyBroker, NautilusTrader, paper trading, testnet, or live environments.

## Adoption boundary

Research-only. This record is a theoretical knowledge capture and hypothesis formulation. It does not constitute an approved strategy, does not demonstrate profitable alpha, and provides zero authorization for implementation, paper trading, testnet deployment, or live capital commitment.

## Related Wiki records

- `diffusive-price-dynamics-square-root-impact-lmf-levy-walk-2026-09-17.md` (Sato et al. 2026: solving the diffusive paradox via event-time Lévy walks)
- `portfolio-representation-switching-frictions-order-flow-long-memory-2026-09-17.md` (Rodríguez Domínguez 2026: switching frictions and order-flow memory)
- `duration-aware-bocpd-lognormal-order-flow-regime-2026-09-11.md` (Jebali 2026: duration-aware changepoints in order flow)
- `fifo-queue-partial-identification-l2-execution-sensitivity-2026-09-16.md` (Danait et al. 2026: partial identification of execution under snapshot intervals)
- `model-free-passive-execution-order-level-shadowing-ppov-2026-09-17.md` (Maciejewski 2026: passive queue shadowing without impact kernels)

## Sources

- **Primary Preprint:** Christopher Angstmann and Tim Gebbie, *"Event-Time Order-Flow Memory, Operational-Time Impact, and Subordinated Market Observables"*, arXiv preprint `arXiv:2609.13715v1 [q-fin.TR, math-ph, math.MP, physics.soc-ph, q-fin.ST]`, submitted September 12, 2026.
  - Journal Status: Accepted for publication in *Journal of Statistical Mechanics: Theory and Experiment* (JSTAT).
  - Abstract URL: https://arxiv.org/abs/2609.13715
  - HTML Full Text: https://arxiv.org/html/2609.13715v1
  - PDF Full Text: https://arxiv.org/pdf/2609.13715v1
  - Canonical DOI: https://doi.org/10.48550/arXiv.2609.13715
