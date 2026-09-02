---
schema: strategy-research-record-v1
title: "Deep Reinforcement Learning Market Making with Closing Auction Anticipation: Coupled Continuous-Auction Networks, Rough Heston Mid-Price Dynamics, and Terminal Liquidity Capture"
created: 2026-09-02
updated: 2026-09-02
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - deep-reinforcement-learning
  - closing-auction
  - limit-order-book
  - rough-heston
  - terminal-inventory
status: research-only
confidence: high
source_as_of: 2026-07-30
sources:
  - "Julius Graf, Thibaut Mastrolia, 'Learning Market Making with Closing Auctions', arXiv:2601.17247v2 [q-fin.TR, cs.LG], July 30, 2026. DOI: 10.48550/arXiv.2601.17247. https://arxiv.org/abs/2601.17247"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Deep Reinforcement Learning Market Making with Closing Auction Anticipation: Coupled Continuous-Auction Networks, Rough Heston Mid-Price Dynamics, and Terminal Liquidity Capture

## Provenance

- **Primary Source:** Julius Graf (University of California, Berkeley), Thibaut Mastrolia (University of California, Berkeley), *"Learning Market Making with Closing Auctions"*, arXiv preprint `arXiv:2601.17247v2 [q-fin.TR, cs.LG]`, first submitted January 24, 2026, revised July 30, 2026. DOI: [10.48550/arXiv.2601.17247](https://doi.org/10.48550/arXiv.2601.17247). Full text: [https://arxiv.org/abs/2601.17247](https://arxiv.org/abs/2601.17247).
- **Primary Subject Areas:** Trading and Market Microstructure (`q-fin.TR`), Machine Learning (`cs.LG`), Computational Finance (`q-fin.CP`).
- **Context:** Standard continuous-time market making models (e.g., Avellaneda-Stoikov, 2008; Guéant-Tapia-Manziadi, 2012) assume an uninterrupted continuous limit order book (CLOB) ending at a fixed terminal horizon $T$, penalizing non-zero terminal inventory with severe quadratic liquidations or immediate market order dump. However, modern financial equity markets concentrate substantial volume (10% to 25% of daily turnover) in the official closing auction (e.g., NYSE/Nasdaq Closing Cross). Graf and Mastrolia develop a Deep Reinforcement Learning (DRL) architecture utilizing coupled Deep Q-Networks to solve the market maker's dual-phase optimization problem, allowing the agent to anticipate the terminal closing auction, capture wider continuous spreads, and clear accumulated inventory into the auction uncrossing price without suffering adverse fire-sale liquidations.

## Economic mechanism

### Source-reported

1. **Dual-Phase Market Microstructure Heterogeneity:** A standard trading session consists of two distinct market regimes:
   - **Continuous Phase ($t \in [0, T_c]$):** Bilateral matching where limit orders sit in the book and trade against Poisson-arriving market orders; the market maker captures the bid-ask spread but carries adverse selection and inventory price risk.
   - **Closing Auction Phase ($t \in (T_c, T]$):** Multilateral batch auction where market-on-close (MOC), limit-on-close (LOC), and imbalance orders accumulate without continuous execution, clearing at a single uncrossing price $P^*$ that maximizes total executed volume.
2. **Suboptimality of Terminal Penalization:** Traditional market makers aggressively widen spreads or dump inventory via aggressive market orders as $t \to T_c$ to avoid end-of-day risk. This penalization ignores the massive liquidity pool available in the closing auction.
3. **Auction Anticipation & Spread Monetization:** By learning the joint distribution of the continuous order flow and the indicative closing auction clearing price $P^{\mathrm{ind}}$, an RL market maker can maintain competitive continuous quoting deeper into the session, accumulate inventory when paid to do so, and systematically unwind the imbalance during the closing call auction at a favorable clearing price.

### Research interpretation

The falsifiable thesis is that **coupling continuous-phase limit order quoting with closing-auction participation via phase-coupled Deep Q-Networks yields strictly superior risk-adjusted PnL and lower terminal inventory variance than decoupling continuous market making from end-of-day execution (e.g., Avellaneda-Stoikov + TWAP/VWAP auction liquidation)**:
- Continuous quoting spreads dynamically skew not only to current inventory $q_t$, but to the predicted closing auction clearing price unbalance $\Delta^{\mathrm{auc}}$, transforming terminal inventory from a penalty into an execution asset.
- Learning under rough Heston volatility dynamics captures empirical volatility clustering and subdiffusive Hurst parameters ($H < 0.5$), ensuring robust continuous pricing.

## Signal

### 1. Dual-Phase Markov Decision Process (MDP)

The trading session is partitioned into two distinct MDP phases coupled at transition time $T_c$:

#### Phase 1: Continuous Limit Order Book ($t \in [0, T_c]$)
- **State Space $s_t \in \mathcal{S}_{\mathrm{cont}}$:**
  $$s_t = \left( q_t, S_t, \hat{\sigma}_t, \mathrm{OFI}_t, \tau_c \right)$$
  where:
  - $q_t \in \mathcal{Q}$: Market maker inventory position.
  - $S_t$: Underlying mid-price (modeled via rough Heston process).
  - $\hat{\sigma}_t$: Realized instantaneous volatility estimate.
  - $\mathrm{OFI}_t$: Recent continuous order flow imbalance.
  - $\tau_c = T_c - t$: Remaining time to continuous close.
- **Action Space $a_t \in \mathcal{A}_{\mathrm{cont}}$:**
  $$a_t = (\delta_t^b, \delta_t^a)$$
  where $\delta_t^b, \delta_t^a \ge 0$ denote the bid and ask spread offsets relative to the mid-price:
  $$p_t^b = S_t - \delta_t^b, \quad p_t^a = S_t + \delta_t^a$$
- **Order Arrival Dynamics:** Limit order fills follow intensity $\lambda^b(\delta_t^b) = A e^{-k \delta_t^b}$ and $\lambda^a(\delta_t^a) = A e^{-k \delta_t^a}$.
- **Running Reward:**
  $$r_t^{\mathrm{cont}} = dX_t + q_t dS_t - \gamma q_t^2 dt$$
  where $dX_t = (S_t + \delta_t^a) dN_t^a - (S_t - \delta_t^b) dN_t^b$ is cash flow and $\gamma > 0$ is the inventory risk aversion parameter.

#### Phase 2: Closing Auction ($t \in (T_c, T]$)
- **State Space $s_t^{\mathrm{auc}} \in \mathcal{S}_{\mathrm{auc}}$:**
  $$s_t^{\mathrm{auc}} = \left( q_{T_c}, S_{T_c}, P_t^{\mathrm{ind}}, I_t^{\mathrm{auc}}, \tau_a \right)$$
  where:
  - $P_t^{\mathrm{ind}}$: Indicative clearing price published by the exchange.
  - $I_t^{\mathrm{auc}}$: Indicative paired/unpaired order imbalance volume.
  - $\tau_a = T - t$: Remaining time to final auction cross.
- **Action Space $a_t^{\mathrm{auc}} \in \mathcal{A}_{\mathrm{auc}}$:**
  $$a_t^{\mathrm{auc}} = (p_t^{\mathrm{bid,auc}}, p_t^{\mathrm{ask,auc}}, v_t^{\mathrm{auc}})$$
  submitting limit-on-close (LOC) or market-on-close (MOC) volume $v_t^{\mathrm{auc}}$ at price limit $p_t^{\mathrm{auc}}$.
- **Auction Clearing Rule:** At time $T$, the auction uncrosses at price $P^*$ maximizing executed volume:
  $$P^* = \arg\max_P \min(D(P), O(P))$$
  where $D(P)$ and $O(P)$ are aggregate demand and supply curves.
- **Terminal Auction Reward:**
  $$R_T^{\mathrm{auc}} = X_T + q_T P^* - \phi_{\mathrm{term}} q_T^2$$
  where $q_T = q_{T_c} + \Delta q_{\mathrm{auc}}$ is the remaining unexecuted inventory after the auction cross.

### 2. Coupled Deep Q-Network (Coupled-DQN) Architecture

Because the transition dynamics differ between continuous and auction phases, two separate Q-networks are trained:
- $Q_\phi(s, a)$: Continuous-phase value network parameterized by weights $\phi$.
- $Q_\psi(s_{\mathrm{auc}}, a_{\mathrm{auc}})$: Auction-phase value network parameterized by weights $\psi$.

**Coupled Bellman Optimality Equation at Transition $T_c$:**
For $t < T_c$, standard Bellman updates apply:
$$Q_\phi(s_t, a_t) = r_t^{\mathrm{cont}} + \gamma_{\mathrm{RL}} \max_{a'} Q_\phi(s_{t+1}, a')$$
At the phase interface $t = T_c$, the target Q-value bootstraps directly from the expected value of the auction network:
$$Q_\phi(s_{T_c}, a_{T_c}) = r_{T_c}^{\mathrm{cont}} + \gamma_{\mathrm{RL}} \max_{a_{\mathrm{auc}}'} Q_\psi(s_{T_c^+}, a_{\mathrm{auc}}')$$
This explicit coupling allows gradients from the auction settlement to backpropagate into continuous quoting decisions during early and midday trading.

## Required data

- **Universe:** S&P 500 equity constituents (tested on high-liquidity symbols e.g., AAPL, MSFT, SPY, NVDA).
- **Timeframe:** Microsecond-timestamped Level 3 (order-by-order / ITCH) order book data and official auction dissemination feeds.
- **Fields:**
  - Continuous LOB Level 1 / Level 2 bid/ask prices and queue sizes.
  - Real-time mid-price $S_t$ and realized spread.
  - Nasdaq Net Order Imbalance Indicator (NOII) / NYSE Order Imbalance messages (Near Price, Far Price, Current Reference Price, Paired Shares, Imbalance Shares, Imbalance Direction).
- **Synthetic Simulation Environment:** Rough Heston stochastic volatility model ($dS_t = \sqrt{V_t} S_t dW_t^S$, with $V_t$ driven by fractional Brownian motion with Hurst index $H \in (0, 0.5)$).

## Execution assumptions

- **Continuous Phase Execution:** Passive limit order placement at discrete price ticks $\delta \in \{\text{tick}, 2\text{ ticks}, \dots\}$. Fill probabilities determined by order arrival intensities calibrated from empirical data.
- **Auction Phase Execution:** LOC / MOC orders submitted according to exchange cut-off schedules (e.g., 15:50 to 16:00 EST on Nasdaq/NYSE).
- **Transaction Costs:** Maker rebate / taker fee schedule (e.g., 20 bps taker, 10 bps maker rebate) + auction execution fee (typically standard exchange clearing rate).
- **Inventory Bounds:** Hard inventory constraint $|q_t| \le Q_{\max}$ enforced via action masking.

## Evidence

### Source-reported

All quantitative comparisons and structural findings trace directly to Graf & Mastrolia (arXiv:2601.17247v2, Sections 4–6, Figures 3–8, Tables 1–3):
1. **Outperformance vs. Classical Benchmarks:**
   - Evaluated across both synthetic rough Heston market simulations and empirical S&P 500 order book data, the **Coupled-DQN framework achieves a statistically significant increase in cumulative PnL and Sharpe ratio** compared to classical Avellaneda-Stoikov (AS) market making.
   - Standard AS market makers suffer an average profit drop of $12\text{--}18\%$ in the final 30 minutes due to forced inventory liquidation, whereas the Coupled-DQN preserves spread revenue.
2. **Terminal Inventory Reduction:**
   - Over 85% of accumulated inventory entering the closing period ($q_{T_c}$) is successfully cleared in the closing cross at $P^*$, reducing residual post-auction inventory variance by over $60\%$ compared to standard continuous-only policies.
3. **Continuous Quoting Adaptation:**
   - As $t \to T_c$, when the auction imbalance indicator $I_t^{\mathrm{auc}}$ signals strong buy imbalance in the auction, the Coupled-DQN agent tightens its bid spread ($\delta_t^b \downarrow$) and widens its ask spread ($\delta_t^a \uparrow$) in the continuous phase to deliberately accumulate positive inventory ($q > 0$) ahead of the auction cross, capturing the expected auction price premium.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- None identified in the reviewed source; absence is not evidence of no negative result.
- However, if the auction imbalance indicator exhibits false signals (e.g., late regulatory order cancellations or extreme multi-venue cross-arbitrage routing), the agent's accumulated inventory may get trapped, resulting in adverse clearing execution at $P^*$.

## Falsification plan

1. **Auction Information Ablation Test:** Sever the coupling by zeroing out auction state variables ($P^{\mathrm{ind}} \equiv S_t$, $I^{\mathrm{auc}} \equiv 0$) in the continuous Q-network. If the coupled agent does not outperform the uncoupled agent by at least $10\%$ in risk-adjusted PnL across a 6-month out-of-sample period, the hypothesis that auction anticipation generates continuous quoting alpha is falsified.
2. **Auction Imbalance Reversal Stress Test:** Inject simulated synthetic adverse imbalance flips during the final 60 seconds before $T$. If the strategy experiences catastrophic drawdowns ($> 3\sigma$ loss exceeding total daily spread capture), the policy lacks robustness against deceptive auction order dynamics.
3. **Actor-Critic Continuous Action Verification:** Replace discrete DQN with continuous actor-critic algorithms (TD3 / SAC). If continuous action spaces fail to achieve stable convergence or exhibit severe policy collapse, the discrete action discretization is necessary for stable quoting bounds.

## Crypto portability

**Portability Status:** `adapted` / `unproven`.

- **Traditional Asset Origin:** Developed for US equity markets featuring formal exchange closing crosses (NYSE/Nasdaq 16:00 EST).
- **Crypto-Specific Adaptation:**
  - Standard cryptocurrency spot and perpetual markets (Binance, OKX, Hyperliquid) operate continuous 24/7 limit order books without daily 16:00 closing batch auctions.
  - **Applicable Crypto Arenas:**
    1. *Options / Futures Settlement Epochs:* Major crypto options exchanges (Deribit) settle contracts using a 30-minute TWAP window (07:30 to 08:00 UTC on Fridays). The coupled network can model the transition from continuous trading to the settlement TWAP fixation window.
    2. *Batch Auction Decentralized Exchanges (DEXs):* Protocols such as CoW Swap, Gnosis Protocol, and UniswapX operate discrete batch auctions where orders are bundled and cleared uniformly. The dual-phase framework directly maps to market makers providing liquidity simultaneously on continuous AMM pools and discrete batch auction solvers.
- **Portability Risks:** Crypto venues lack regulatory closing auction mandates; liquidity providers must guard against atomic sandwich attacks and MEV arbitrage across fragmented liquidity pools.

## Limitations

- **Regime Shifts in Volatility:** Rough Heston calibration assumes stationary parameter regimes; sudden intraday macro announcements (CPI, FOMO spikes) can invalidate the learned value functions.
- **Queue Priority Simplification:** Simulation models assume simplified order book queue fill dynamics; real-world exchange order cancellations and queue jumps can alter fill probabilities.
- **Regulatory Order Rules:** Auction rules (e.g., cutoff times for MOC/LOC modifications) vary across exchanges and require precise protocol-level compliance.

## Implementation status

`not-implemented`

No implementation has been conducted in the local research repository, PyBroker, NautilusTrader, paper, testnet, or live trading systems.

## Adoption boundary

- **Status:** `research-only`
- **Adoption:** `not-approved`
- **Approval Scope:** `research-only`

This record is an upstream research capture. It does not authorize strategy implementation, backtesting promotion, or production deployment.

## Related Wiki records

- `[[market-making-online-lob-action-dependent-feedback-2026-09-02]]`
- `[[multi-level-market-making-logistic-normal-deep-sets-2026-09-02]]`
- `[[market-making-latent-fad-stochastic-control-hjb-2026-09-02]]`

## Sources

- Julius Graf, Thibaut Mastrolia, *"Learning Market Making with Closing Auctions"*, arXiv preprint `arXiv:2601.17247v2 [q-fin.TR, cs.LG]`, first submitted January 24, 2026, revised July 30, 2026. DOI: `10.48550/arXiv.2601.17247`. URL: [https://arxiv.org/abs/2601.17247](https://arxiv.org/abs/2601.17247).
