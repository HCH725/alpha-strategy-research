---
schema: strategy-research-record-v1
title: "Dealer Toxic Flow Infinite-Horizon Internalisation-Externalisation and Speculation"
created: 2026-09-17
updated: 2026-09-17
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
status: research-only
confidence: medium
source_as_of: 2025-03-24
sources:
  - https://arxiv.org/abs/2503.18005
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Dealer Toxic Flow Infinite-Horizon Internalisation-Externalisation and Speculation

## Provenance

- **Primary Source:** Álvaro Cartea (University of Oxford, Oxford-Man Institute of Quantitative Finance) and Leandro Sánchez-Betancourt (King's College London / Oxford-Man Institute of Quantitative Finance), *"A Simple Strategy to Deal with Toxic Flow"*, arXiv preprint `arXiv:2503.18005v1 [q-fin.TR]`, submitted March 24, 2025.
- **Canonical arXiv URL:** https://arxiv.org/abs/2503.18005
- **Full Text HTML:** https://arxiv.org/html/2503.18005v1
- **DOI:** https://doi.org/10.48550/arXiv.2503.18005
- **Licence:** Creative Commons Attribution 4.0 International (CC BY 4.0).
- **Deduplication Audit:** A comprehensive audit of all existing strategy records in `alpha-strategy-research` confirmed zero prior records citing `2503.18005` or Sánchez-Betancourt. Existing repository records involving toxic flow focus on automated market maker loss-versus-rebalancing (`crypto-amm-loss-versus-rebalancing-lvr-toxic-arbitrage-2026-08-31.md`), volume-synchronized toxicity (`crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31.md`), or high-frequency Kyle's lambda reversal (`crypto-high-frequency-kyles-lambda-price-impact-reversal-2026-08-31.md`). No existing record covers the infinite-horizon closed-form dealer internalisation-externalisation and speculation strategy or the parameter-free training algorithm formulated by Cartea and Sánchez-Betancourt.

## Economic mechanism

### Source-reported

The authors model the trading interaction between a broker/dealer and her clients (categorized into informed and uninformed traders) as an infinite-horizon stochastic control problem. The lit market mid-price satisfies:
$$dS_t = \alpha_t dt + \sigma^s dW^S_t$$
where $\alpha_t$ is an unobserved mean-reverting alpha drift:
$$d\alpha_t = -\kappa^\alpha \alpha_t dt + \sigma^\alpha dW^\alpha_t$$

An informed client observes $\alpha_t$ and trades with the broker at speed $\nu^I_t = A \alpha_t - B Q^I_t$, balancing exploitation of the trend against quadratic inventory penalties. An uninformed client trades at speed $\nu^U_t$, generating noise volume. The broker does not directly observe $\alpha_t$, but knows the structure of the informed trader's feedback control.

The broker's dealing strategy balances three distinct economic objectives:
1. **Internalisation and externalisation:** internalising uninformed client flow to capture liquidity fees, while externalising toxic client flow into the lit market.
2. **Inventory risk management:** exerting mean-reverting pressure to liquidate accumulated broker inventory back toward zero.
3. **Speculative alpha execution:** extracting the latent market signal $\alpha_t$ from the informed counterparty's observed trading speed $\nu^I_t$ and trading alongside the informed flow in the lit market. When the externalisation coefficient $H > 1$, the broker trades strictly more than the volume dumped by the informed trader, turning adverse selection into a speculative alpha signal.

Furthermore, the paper characterizes the liquidity discount the broker offers clients relative to the lit market to optimally trade off client flow generation against adverse selection losses.

### Research interpretation

The falsifiable hypothesis is that **segmented order flow from identified informed counterparties contains extractable directional alpha that allows an intermediary to achieve net positive risk-adjusted returns by dynamically hedging toxic inventory into public venues while internalizing uninformed retail flow**. 

Rather than treating toxic flow purely as an adverse-selection cost to be avoided by widening spreads or rejecting counterparties, the dealer uses the arrival of informed orders as a real-time predictor of short-term price drift. The strategy decomposes into four operational component roles:
- **Broker Inventory Control:** $-c Q^B_t$, linear inventory decay returning dealer net holdings to neutral.
- **Toxic Inventory Offloading:** $-g Q^I_t$, counteracting inventory acquired from informed counterparties.
- **Informed Flow Piggybacking / Speculation:** $+h V^I_t$, trading in the direction of the informed counterparty's trades (externalizing and, if $h > 1$, front-running/speculating on the drift).
- **Uninformed Flow Hedging:** $+f V^U_t$, partial hedge against uninternalized noise flow.

## Signal

### Continuous-Time Closed-Form Rule (Source-Reported)

From Theorem 2.2, the broker's optimal continuous trading rate $\nu^{B,*}_t$ in the lit market is:
$$\nu^{B,*}_t = -C Q^B_t - D Q^I_t + E \alpha_t + F \nu^U_t$$
Equivalently, expressing $\alpha_t$ via the informed trader's trading speed $\nu^I_t = A \alpha_t - B Q^I_t$:
$$\nu^{B,*}_t = -C Q^B_t - G Q^I_t + H \nu^I_t + F \nu^U_t$$
where:
$$C = \frac{2a^B - b - \mathfrak{q}_2}{2k^B} > 0$$
$$H = \frac{E}{A} = \frac{\mathfrak{d}_0}{4k^B A} > 0$$
$$F = \frac{\mathfrak{d}_2}{4k^B} > 0$$
$$G = D - \frac{B E}{A} = -\frac{\mathfrak{d}_1}{4k^B} - \frac{B \mathfrak{d}_0}{4k^B A}$$

The underlying constants are uniquely given in closed form by:
- Informed trader coefficients (Theorem 2.1):
  $$A = \frac{1}{\beta k^I + 2k^I \kappa^\alpha + \sqrt{4a^I \beta k^I + (\beta k^I)^2 + 2k^I \phi^I}}$$
  $$B = \sqrt{\frac{a^I \beta}{k^I} + \left(\frac{\beta}{2}\right)^2 + \frac{\phi^I}{2k^I}} - \frac{\beta}{2}$$
- Broker value function coefficients:
  $$\mathfrak{q}_2 = 2a^B - b + \beta k^B - \sqrt{4a^B \beta k^B - 2b \beta k^B + \beta^2 (k^B)^2 + 2k^B \phi^B}$$
  $$\mathfrak{d}_2 = 2(2a^B - \mathfrak{q}_2)(\beta + \kappa_u + C)^{-1}$$
  $$\mathfrak{d}_1 = -2B(2a^B - \mathfrak{q}_2)(\beta + B + C)^{-1}$$
  $$\mathfrak{d}_0 = \left[2 + 2A(2a^B - \mathfrak{q}_2) + A \mathfrak{d}_1\right](\beta + \kappa^\alpha + C)^{-1}$$

### Discrete-Time Parameter-Free Trading Algorithm (Source-Reported Algorithm 1)

To bypass calibrating the latent parameters ($\kappa^\alpha, \sigma^\alpha, a^B, b, \beta$), the paper introduces a direct empirical parameter-learning algorithm:
1. Discretize trading time into equal intervals $\Delta > 0$ (source-reported example: $\Delta = 100\text{ ms}$).
2. The volume traded by the broker in the lit market over interval $[(j-1)\Delta, j\Delta]$ is:
   $$V^{B}_{j\Delta} = -c Q^B_{(j-1)\Delta} - g Q^I_{(j-1)\Delta} + h V^I_{j\Delta} + f V^U_{j\Delta}$$
   with $(c, g, h, f) \in \mathbb{R}^+ \times \mathbb{R} \times \mathbb{R}^+ \times \mathbb{R}^+$.
3. The broker's state transitions:
   - Informed inventory: $Q^I_{j\Delta} = Q^I_{(j-1)\Delta} + V^I_{j\Delta}$
   - Broker inventory: $Q^B_{j\Delta} = Q^B_{(j-1)\Delta} - V^I_{j\Delta} - V^U_{j\Delta} + V^B_{j\Delta}$
   - Cash process: $X^B_{j\Delta} = X^B_{(j-1)\Delta} + V^I_{j\Delta} \hat{S}^I_{j\Delta} + V^U_{j\Delta} \hat{S}^U_{j\Delta} - V^B_{j\Delta} \hat{S}^B_{j\Delta}$
     where $\hat{S}^I, \hat{S}^U, \hat{S}^B$ are the execution prices.
4. Objective function to maximize over historical training days $\mathfrak{O} = \{1, \dots, \tilde{N}\}$:
   $$P(c, g, h, f) = \frac{1}{\tilde{N}} \sum_{i=1}^{\tilde{N}} P^i$$
   where single-day performance $P^i$ includes terminal wealth and cumulative inventory penalty:
   $$P^i = X^{i,B}_{\tilde{M}\Delta} + Q^{i,B}_{\tilde{M}\Delta} S^i_{\tilde{M}\Delta} - a^B (Q^{i,B}_{\tilde{M}\Delta})^2 - \phi^B \sum_{j=1}^{\tilde{M}} (Q^{i,B}_{j\Delta})^2 \Delta$$

### Operational Rules and Research-Proposed Specifications

- **Client Toxicity Profiling:** Counterparties are classified into informed ($V^I$) and uninformed ($V^U$) via trade markout profiling (Cartea et al. 2023, cited in Section 3.1). A client whose trades exhibit positive median markout over $0$ to $10$ seconds post-trade is classified as informed.
- **Classification Threshold:** `research-proposed`: markout cutoff of $+0.5\text{ bps}$ at $t = 5\text{ seconds}$ post-trade to designate a counterparty as informed.
- **Execution Interval:** Source-reported example is $\Delta = 100\text{ ms}$; for crypto perpetuals / CEX liquidity provision, $\Delta = 250\text{ ms}$ is `research-proposed`.
- **Lit Market Order Type:** `research-proposed`: lit market rebalancing volume $V^B$ is submitted as aggressive immediate-or-cancel (IOC) taker orders to guarantee immediate execution against the top of the order book.
- **Position Limits:** `research-proposed`: hard risk ceiling $|Q^B_t| \le Q_{\max}$ with circuit-breaker flattening if inventory exceeds $2 \times Q_{\max}$.

## Required data

- **Client Trade Feed:** Counterparty account identifier, fill timestamp (microsecond/millisecond precision), executed volume ($V^I, V^U$), side (buy/sell), and executed quote price ($\hat{S}^I, \hat{S}^U$).
- **Reference Market Feed:** Top-of-book lit market prices ($S_t$), best bid/ask quotes, and external execution fills ($V^B, \hat{S}^B$).
- **Historical Order Archive:** Multi-day historical record of client executions and reference mid-prices for offline optimization of $(c^*, g^*, h^*, f^*)$ via Algorithm 1.
- **Point-in-Time Availability:** The broker's decision at step $j\Delta$ relies strictly on past inventory states $Q^B_{(j-1)\Delta}, Q^I_{(j-1)\Delta}$ and contemporaneous incoming client flow $V^I_{j\Delta}, V^U_{j\Delta}$. No future reference prices are permitted.
- **Crypto-Specific Data:** Centralized exchange Level 2 depth feeds (Binance, Bybit, OKX) or OTC RFQ message streams (Paradigm) with client identification tags.

## Execution assumptions

- **Source-Reported Assumptions:**
  - Continuous lit market price impact is linear: $\hat{S}^B_t = S_t + k^B \nu^B_t$ with baseline parameter $k^B = 1.2 \times 10^{-3}$.
  - Client bespoke execution prices incorporate linear liquidity costs: $\hat{S}^I_t = S_t + k^I \nu^I_t$ and $\hat{S}^U_t = S_t + k^U \nu^U_t$.
  - Broker inventory holding penalty: running penalty $\phi^B (Q^B_t)^2$ with $\phi^B = 10^{-2}$ and terminal penalty $a^B (Q^B)^2$ with $a^B = 1$.
  - Continuous or discrete frictionless order reception from clients without queuing latency.
- **Research-Proposed Operational Assumptions:**
  - Lit market fills incur standard venue taker fees (e.g. $2.0$ to $4.0\text{ bps}$) plus half-spread crossing costs.
  - Execution latency between receiving client flow and routing $V^B$ to the lit market is assumed to be $\tau \approx 10\text{ ms}$ (`research-proposed`).
  - Partial fills on external lit orders are handled by clipping $V^B$ to available Level 1 depth, carrying residual inventory to the subsequent interval $(j+1)\Delta$ (`research-proposed`).

## Evidence

### Source-reported

All numerical and comparative results below are directly reported by Álvaro Cartea and Leandro Sánchez-Betancourt in arXiv:2503.18005v1 (Section 3, Figures 1–4):
- **Simulation Setup:**
  - Time horizon: infinite horizon with discount rate $\beta = 0.01$.
  - Initial states: $x^B = x^I = q^I = q^B = 0$, $S_0 = 100$, $\alpha_0 = 0$, $\nu^U_0 = 0$.
  - Alpha and price dynamics: $\kappa^\alpha = 5$, $\sigma^\alpha = 1$, $\sigma^s = 1$.
  - Uninformed trader dynamics: mean-reversion speed $\kappa_u = 15$, volatility $\sigma^U = 100$.
  - Transaction cost and impact parameters: $k^I = k^U = 1.0 \times 10^{-3}$, $k^B = 1.2 \times 10^{-3}$.
  - Penalty parameters: $a^I = a^B = 1$, $\phi^B = \phi^I = 10^{-2}$.
  - The authors note that this calibration ensures broker losses to the informed trader are of the same order of magnitude as profits earned from the uninformed trader.
- **Key Quantitative Findings:**
  - **Optimal Liquidity Discount:** The broker maximizes her value function when the liquidity costs charged to both informed and uninformed clients are approximately **60% of the liquidity cost in the lit market** ($k^I / k^B \approx 0.60$ and $k^U / k^B \approx 0.60$; Figure 4).
  - **Client Cost Tradeoff:** As liquidity cost $k^U$ charged to uninformed clients increases toward $k^B$, uninformed volume decreases according to equation (80), eventually dropping to zero as $k^U \nearrow k^B$ because liquidity becomes too expensive.
  - **Speculation Threshold:** When $H = E/A > 1$, the broker trades in the lit market at a rate strictly exceeding the volume of the informed trader, demonstrating that the optimal response is not merely passive hedging but active directional speculation.
  - **Sensitivity to Informed Penalty:** Lower inventory aversion $\phi^I$ by the informed trader severely degrades the broker's value function, as the informed trader becomes much more aggressive in exploiting the alpha drift $\alpha_t$ (Figure 1).

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Source-Reported Breakdown Modes:**
  - When lit market transaction costs $k^B$ exceed client liquidity charges $k^I, k^U$ by a significant margin, the broker's value function turns negative (Figure 2, left panel, blue region).
  - If informed traders operate with near-zero inventory penalties ($\phi^I \to 0$), the broker incurs catastrophic adverse selection losses that cannot be offset by uninformed client fees (Figure 1, right panel).
- **External Literature / Review Evidence:**
  - None identified in the reviewed source; absence is not evidence of no negative result.

## Falsification plan

1. **Placebo Client Labeling Test:**
   - Shuffle client identity labels randomly between informed and uninformed pools prior to running Algorithm 1.
   - *Research-defined falsification threshold:* If the PnL of strategy $(c^*, g^*, h^*, f^*)$ trained on shuffled labels does not degrade by at least $40\%$ relative to the true-label strategy, the hypothesis that informed flow contains actionable predictive alpha is falsified.
2. **External Execution Latency Stress Test:**
   - Inject synthetic latency $\tau \in \{5\text{ ms}, 25\text{ ms}, 50\text{ ms}, 100\text{ ms}, 250\text{ ms}\}$ into lit market order routing for $V^B$.
   - *Research-defined falsification threshold:* If net speculative PnL turns negative at latency $\tau \le 50\text{ ms}$, the practical viability of speculative piggybacking is falsified for non-co-located participants.
3. **Walk-Forward Parameter Stability Test:**
   - Train $(c^*, g^*, h^*, f^*)$ on $\tilde{N} = 20$ days and test out-of-sample on the subsequent $5$ days across 10 rolling folds.
   - *Research-defined falsification threshold:* If out-of-sample Sharpe ratio drops below $0.0$ or net profit after costs is negative in more than 3 out of 10 folds, the parameter-free stationary representation is falsified.
4. **Adverse Fee / Spread Crossing Hurdle:**
   - Replace the continuous quadratic cost $k^B (\nu^B)^2$ with realistic exchange taker fee tiers ($4\text{ bps}$) and finite order book depth.
   - *Research-defined falsification threshold:* If total fee expenditure exceeds cumulative spread capture from uninformed flow plus alpha gain from informed flow, the commercial viability is falsified.

## Crypto portability

**adapted / unproven**

- The paper's theoretical framework and empirical calibration are derived from traditional OTC broker-dealer markets (spot foreign exchange as in Cartea & Sánchez-Betancourt 2023, and equity markets as in Cartea & Jaimungal 2016). The authors do not examine cryptocurrency markets.
- Applying this model to crypto represents an adaptation suitable for:
  - Institutional crypto OTC liquidity providers (e.g. Wintermute, Cumberland) receiving bilateral RFQs.
  - Decentralized RFQ platforms (e.g. Paradigm, Hashflow) where taker addresses can be profiled on-chain.
  - High-tier centralized exchange market makers (Binance, Bybit) who can segment flow across sub-accounts or observe specific API trader latency profiles.
- **Crypto Portability Risks:**
  - **24/7 Continuous Trading:** Crypto lacks fixed daily closing horizons ($M\Delta = T$). The daily summation in equation (83) must be adapted to rolling continuous evaluation windows.
  - **Pseudonymous Counterparty Switching:** In crypto, informed traders frequently rotate wallet addresses and exchange sub-accounts to evade toxic profiling, breaking the client classification premise.
  - **Perpetual Funding Rate Drag:** Holding hedge inventory $Q^B$ overnight in crypto perpetuals exposes the broker to funding rate bleed during crowded market regimes.
  - **Cross-Exchange Latency Arbitrage:** Crypto price discovery is fragmented across multiple global venues (Binance, Bybit, OKX, Coinbase). Hedging on a single lit venue exposes the dealer to lead-lag toxic sniping from external venues.

## Limitations

- **Counterparty Segmentation Dependency:** The strategy fundamentally relies on pre-classifying counterparties into informed vs. uninformed classes. In real-world decentralized or anonymous order books, identifying counterparties in real time is severely constrained.
- **Stylized Execution Frictions:** The source assumes linear price impact $k^B \nu^B$ and frictionless continuous order streaming, ignoring discrete queue positions, tick sizes, maker/taker fee asymmetries, and cancel/replace latencies.
- **Simulation-Only Empirical Validation:** The source provides numerical value function evaluations across calibrated parameters rather than a live empirical backtest on tick data. Real-world Sharpe, CAGR, and drawdown metrics are therefore **underspecified** in the primary source.
- **Convexity of Parameter Optimization:** Algorithm 1 assumes optimization over $(c, g, h, f)$ can be executed reliably on historical days, but the paper does not prove global convexity of the objective function $P(c, g, h, f)$.
- **Not Independently Reproduced:** All quantitative claims reflect source-reported numerical evaluations only.

## Implementation status

`not-implemented`

No prototype or validation script has been implemented in our research stack (`nautilus-quant-system`, PyBroker, or NautilusTrader). This record is an upstream research capture only.

## Adoption boundary

`research-only` | `adoption: not-approved` | `approval_scope: research-only`

This research capture does not constitute trading authorization, does not establish a verified production alpha, and does not approve implementation for paper, testnet, or live trading.

## Related Wiki records

No stable Hermes Wiki Brain link is asserted from this GitHub-only Scout run.

## Sources

- **Primary Paper:** Álvaro Cartea and Leandro Sánchez-Betancourt, *"A Simple Strategy to Deal with Toxic Flow"*, arXiv preprint `arXiv:2503.18005v1 [q-fin.TR]`, submitted March 24, 2025.
  - Canonical URL: https://arxiv.org/abs/2503.18005
  - HTML Full Text: https://arxiv.org/html/2503.18005v1
  - DOI: https://doi.org/10.48550/arXiv.2503.18005
- **Related Prior Literature Cited in Primary Source:**
  - Álvaro Cartea and Leandro Sánchez-Betancourt (2022), *"Brokers and informed traders: dealing with toxic flow and extracting trading signals"*, forthcoming in *SIAM Journal on Financial Mathematics*.
  - Álvaro Cartea, G. Duran-Martin, and Leandro Sánchez-Betancourt (2023), *"Detecting toxic flow"*, arXiv preprint `arXiv:2312.05827`.
  - Álvaro Cartea and Sebastian Jaimungal (2016), *"Incorporating order-flow into optimal execution"*, *Mathematics and Financial Economics*, 10(3):339–364.
  - Álvaro Cartea and Leandro Sánchez-Betancourt (2023), *"Optimal execution with stochastic delay"*, *Finance and Stochastics*, 27(1):1–47.
