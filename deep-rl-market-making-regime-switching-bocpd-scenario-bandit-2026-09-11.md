---
schema: strategy-research-record-v1
title: "Deep Reinforcement Learning Market Making under Regime-Switching Order Flow: Distributional DQN with Bayesian Online Changepoint Filtering and Scenario-Bandit Robust Fine-Tuning"
created: 2026-09-11
updated: 2026-09-11
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-making
  - reinforcement-learning
  - distributional-dqn
  - c51
  - rainbow-dqn
  - order-flow-regimes
  - bayesian-online-changepoint-detection
  - smdp
  - limit-order-book
  - inventory-risk
status: research-only
confidence: high
source_as_of: 2026-09-10
sources:
  - "Felipe Moret and Fabrizio Lillo, 'Deep Learning of Robust Market Making under Regime-Switching Order Flow', arXiv:2609.11614v1 [q-fin.TR, cs.LG, q-fin.CP], September 10, 2026. https://arxiv.org/abs/2609.11614"
  - "https://github.com/felipemoret77/robust-deep-market-making (commit 395aed7ce98d97684496bc7e3c23a2e64385630a, 2026-09-10)"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Deep Reinforcement Learning Market Making under Regime-Switching Order Flow: Distributional DQN with Bayesian Online Changepoint Filtering and Scenario-Bandit Robust Fine-Tuning

## Provenance

- **Primary Source:** Felipe Moret (Scuola Normale Superiore, Pisa, Italy, `felipe.moret@sns.it`) and Fabrizio Lillo (Scuola Normale Superiore, Pisa, Italy and Università di Bologna, Bologna, Italy, `fabrizio.lillo@sns.it`), *"Deep Learning of Robust Market Making under Regime-Switching Order Flow"*, arXiv preprint `arXiv:2609.11614v1 [q-fin.TR, cs.LG, q-fin.CP]`, submitted September 10, 2026.
  - Stable arXiv URL: https://arxiv.org/abs/2609.11614
  - Full-text HTML: https://arxiv.org/html/2609.11614v1
  - Full-text PDF: https://arxiv.org/pdf/2609.11614v1
  - Canonical DOI: [10.48550/arXiv.2609.11614](https://doi.org/10.48550/arXiv.2609.11614)
- **Primary Code Implementation:** Public GitHub repository `https://github.com/felipemoret77/robust-deep-market-making`
  - Full immutable commit SHA: `395aed7ce98d97684496bc7e3c23a2e64385630a` (as-of September 10, 2026)
  - Key source paths:
    - [`src/agents/DeepSarsaQRunner.py`](https://github.com/felipemoret77/robust-deep-market-making/blob/395aed7ce98d97684496bc7e3c23a2e64385630a/src/agents/DeepSarsaQRunner.py): Algorithm A (stationary Rainbow DQN controller)
    - [`src/agents/DeepSarsaQRunner_REGIME.py`](https://github.com/felipemoret77/robust-deep-market-making/blob/395aed7ce98d97684496bc7e3c23a2e64385630a/src/agents/DeepSarsaQRunner_REGIME.py): Algorithm B (regime-aware fine-tuning with Bayesian flow filter and quote-exposure imbalance)
    - [`src/agents/DeepSarsaQRunner_RANDOM_TAU.py`](https://github.com/felipemoret77/robust-deep-market-making/blob/395aed7ce98d97684496bc7e3c23a2e64385630a/src/agents/DeepSarsaQRunner_RANDOM_TAU.py): Algorithm C (scenario-bandit robust fine-tuning)
    - [`src/sim/DeepRLController.py`](https://github.com/felipemoret77/robust-deep-market-making/blob/395aed7ce98d97684496bc7e3c23a2e64385630a/src/sim/DeepRLController.py): Market-making quoting logic, FIFO queue management, action-space projection, and safety clamping
    - [`src/sim/lob_simulator.py`](https://github.com/felipemoret77/robust-deep-market-making/blob/395aed7ce98d97684496bc7e3c23a2e64385630a/src/sim/lob_simulator.py): Continuous-time event-driven Santa Fe limit order book simulator with order-level FIFO queue tracking
    - [`src/glft/GLFTPolicy.py`](https://github.com/felipemoret77/robust-deep-market-making/blob/395aed7ce98d97684496bc7e3c23a2e64385630a/src/glft/GLFTPolicy.py): Calibrated Guéant–Lehalle–Fernandez-Tapia (2013) benchmark policy
- **Calibration Sample:** Level-3 order-book data for Amazon (`AMZN`) from the LOBSTER dataset covering 28 trading days from August 1, 2025 to September 10, 2025 (regular trading session 09:30–16:00 ET, excluding the first and last 60 minutes to eliminate open/close boundary effects, totaling ~2.9 \times 10^7 Level-3 messages).
- **Repository Deduplication:** Audited all existing `.md` records in `alpha-strategy-research`. Zero prior records cite `arXiv:2609.11614`, Felipe Moret, or this repository. Related market-making captures (`hawkes-driven-otc-market-making-volterra-riccati-2026-09-01.md`, `multi-level-market-making-logistic-normal-deep-sets-2026-09-02.md`, `sinkhorn-robust-rl-high-frequency-market-making-2026-09-02.md`) investigate different frameworks (Hawkes impact kernels, continuous multi-level deep sets, distributionally robust Sinkhorn ambiguity sets); none address distributional DQN with Bayesian online changepoint filtering and scenario-bandit curriculum fine-tuning under regime-switching order flow.

## Economic mechanism

### Source-reported

Market makers earn the bid-ask spread by continuously posting passive limit orders on both sides of a limit order book (LOB), supplying immediacy to incoming aggressive market orders. Classical stochastic-control solutions, notably Avellaneda & Stoikov (2008) and the Guéant–Lehalle–Fernandez-Tapia (GLFT, 2013) extension, deliver closed-form optimal quoting rules under the foundational assumption of stationary Poisson order flow with symmetric buy/sell intensities.

In real financial markets, however, order flow is deeply non-stationary and episodic: institutional participants break large metaorders into sequences of child orders (TWAP/VWAP executions), and crowded positioning creates persistent directional imbalance. When exposed to persistent directional regimes, both GLFT and stationarily trained reinforcement learning market makers suffer catastrophic failure:
1. **Inventory Saturation:** Unilateral aggressive market orders relentlessly execute against the market maker's quote on the absorbing side (e.g. persistent sell orders hitting the market maker's bid). The market maker accumulates inventory until it hits its hard position cap ($|q_t| = q_{\max}$).
2. **Quote Suppression & Adverse Selection:** Once the hard inventory cap is hit, quote-gating must disable posting on that side to prevent inventory breach. The market maker is stripped of two-sided spread capture, left with trapped inventory, and suffers compounding mark-to-market adverse-selection losses as the directional flow drifts the mid-price adversely.

To overcome this, Moret and Lillo construct a three-stage reinforcement-learning pipeline:
- **Algorithm A (Stationary Rainbow DQN):** Formulates market making as a throttled semi-Markov decision process (SMDP) controlling a Rainbow Distributional DQN (C51 dueling network, 101 atoms on support $[-3, 3]$) in an event-driven FIFO LOB. Rainbow C51 models the full return distribution rather than a scalar Q-value, capturing the heavy-tailed, asymmetric PnL of limit-order fills. Algorithm A strictly dominates GLFT across the entire risk-return frontier in stationary markets, but remains vulnerable to persistent regimes.
- **Algorithm B (Regime-Aware Fine-Tuning):** Augments the agent's state with two belief-style auxiliary signals:
  1. *Bayesian Online Changepoint Detection (BOCPD):* Adapts Adams & MacKay (2007) to the signed market-order stream on the market-order event clock, delivering a posterior directional bias $\widehat{\iota}_t = 2\widehat{p}_t - 1$ and posterior expected regime run length $\bar{\ell}_t$.
  2. *Queue-Adjusted Quote-Exposure Imbalance:* An instantaneous feature $x_t \in [-0.5, 0.5]$ evaluating the agent's net fill vulnerability given its active orders and their depth in the FIFO queue.
  Fine-tuning the stationary policy on regime-switching order flow restores profitability and prevents inventory saturation by dynamically widening or withdrawing quotes on the pressured side.
- **Algorithm C (Scenario-Bandit Robust Fine-Tuning):** Addresses remaining lower-tail risk under out-of-distribution regime persistence and correlated directional switches. A non-stationary multi-armed bandit maintains a pool of $M = 256$ exogenous regime scenarios, dynamically upweighting scenarios where the current policy experienced high penalized terminal losses. This curriculum concentrates training on adverse realizations without changing the state representation.

### Research interpretation

The core economic insight is that market making under non-stationary order flow cannot be solved by simply adding more training data or larger neural networks to an average-case objective. Passive limit orders earn a positive margin in balanced regimes, but possess strongly negative conditional expected returns upon the arrival of institutional metaorders. 

By separating latent regime inference (via analytical Bayesian filtering on the market-order clock) from execution control (via deep reinforcement learning on a throttled decision clock), the architecture achieves structural sample efficiency. The agent receives calibrated probabilistic summaries of the market's hidden state, allowing the policy to internalize the asymmetric risk-reward of holding inventory during trending regimes. The scenario bandit operates as an adversarial curriculum, directly attacking the left tail of the PnL distribution.

## Signal

### Decision Clock & SMDP Throttling
The agent operates on a throttled decision grid in simulated physical time $\tau_c = 1.0\,\mathrm{s}$ (`source-reported`), distinct from the underlying continuous-time LOB event clock. A decision is evaluated when the simulator clock has advanced by at least $\tau_c$ seconds since the prior decision.
- On average, $\bar{N}_t \approx 6$ raw LOB events (LO arrivals, MO arrivals, cancellations) occur between decision epochs (`source-reported`).
- To maintain Bellman consistency across variable inter-decision event counts $N_t \ge 1$, rewards are discounted by within-interval event offset:
  $$r_t = \sum_{n=0}^{N_t - 1} \gamma^n r_{t,n}$$
  where $\gamma = 1 - 10^{-3} = 0.999$ per event (`source-reported`), and the effective transition discount is $\Gamma_t = \gamma^{N_t}$.

### State Representation
The agent observes a compact state vector:
$$s_t = \bigl[ \mathrm{spr}_t,\, d_{t,0}^b,\, d_{t,1}^b,\, d_{t,0}^a,\, d_{t,1}^a,\, q_t,\, e_t \bigr]$$
where:
- $\mathrm{spr}_t = A_t - B_t$: Touch spread in integer ticks (`source-reported`).
- $d_{t,k}^b, d_{t,k}^a$: Queue depth (integer lot count) at offset $k \in \{0, 1\}$ from the best bid $B_t$ and best ask $A_t$ ($d=0$ if empty) (`source-reported`).
- $q_t \in \{-q_{\max}, \ldots, +q_{\max}\}$: Signed inventory lot count, with hard cap $q_{\max} = 8$ units (`source-reported`).
- `has_bid`, `has_ask`: Internal binary indicators tracking active resting quotes (`source-reported`).
- $e_t$: Auxiliary order-flow feature vector (`source-reported`):
  - In Algorithm A (stationary): $e_t = \emptyset$.
  - In Algorithm B and C: $e_t = (b_t, x_t)$, where:
    1. $b_t = (\widehat{\iota}_t, \bar{\ell}_t)$: Bayesian online changepoint summary (`source-reported`). On each market order $y_m \in \{-1, +1\}$, the filter updates run-length probabilities $g_m(\ell)$ using a conjugate Beta-Bernoulli segment model with prior $\mathrm{Beta}(a_0, b_0)$ ($a_0 = b_0 = 1$) and constant hazard $h = 1/\tau_r$. The controller reads:
       $$\widehat{\iota}_t = 2\widehat{p}_t - 1 \in [-1, 1], \quad \bar{\ell}_t = \sum_{\ell \ge 1} \ell \, g_t(\ell)$$
    2. $x_t \in [-0.5, 0.5]$: Instantaneous queue-adjusted quote-exposure imbalance (`source-reported`):
       $$x_t = \frac{1}{2} \left[ \frac{\mathbb{I}(\text{bid live})}{1 + \mathrm{qa}_t^b} - \frac{\mathbb{I}(\text{ask live})}{1 + \mathrm{qa}_t^a} \right]$$
       where $\mathrm{qa}_t^b, \mathrm{qa}_t^a$ are the number of resting units ahead of the MM's quote in the FIFO queue.

### Action Space
The policy selects from a discrete 6-element quote-offset grid (`source-reported`):
$$\mathcal{A} = \bigl\{ (-1,-1),\, (-1,0),\, (0,-1),\, (0,0),\, (0,+1),\, (+1,0) \bigr\}$$
where each action specifies offsets $(\Delta_b, \Delta_a)$ relative to current touch $(B_t, A_t)$:
$$p_t^b = B_t - \Delta_b \cdot v_{\mathrm{tick}}, \quad p_t^a = A_t + \Delta_a \cdot v_{\mathrm{tick}}$$
- $\Delta = 0$: Joins the back of the queue at the current touch.
- $\Delta = +1$: Posts 1 tick deeper into the book (wider spread, lower fill probability, higher spread capture).
- $\Delta = -1$: Posts 1 tick inside the spread (creates a new best quote, standalone at front of queue).
- Ablation finding: The 6-action space removes extreme actions $(+1, +1)$, $(+1, -1)$, $(-1, +1)$, converging substantially better under limited-budget fine-tuning (best training terminal PnL moving average $+0.097$ vs $-0.005$ for 9-action grid, `source-reported`).

### Execution Mechanics & Projection Layers
- **Smart Quoting & Priority Persistence:** At each decision epoch, if the target quote price matches the MM's existing resting quote, the order is left untouched to retain its FIFO priority. If the price changes, the resting order is canceled and reposted at the new price level (`source-reported`).
- **Safety Clamp:** Enforces $p_t^b < p_t^a$. When $(-1, -1)$ is selected on a spread $\le 2$ ticks, quotes are clamped to avoid crossing (binds in ~8% of decisions, `source-reported`).
- **Hard Inventory Projection:** If $q_t = +q_{\max} = +8$, the bid quote is dropped post-hoc; if $q_t = -q_{\max} = -8$, the ask quote is dropped post-hoc. The agent learns the projected consequences without restricting the action space (`source-reported`).

### Reward Specification
The per-decision transition reward is formulated as (`source-reported`):
$$r_t = \sum_{f \in \mathcal{F}_t} \Delta q(f) \bigl( m_{t+1} - p(f) \bigr) - \varphi \, q_{t+1}^2 - w_{\mathrm{inv}} \bigl( |q_{t+1}| - q_w \bigr)_+^2$$
where:
- $\mathcal{F}_t$: Fills executed in interval $(t, t+1]$ ($|\mathcal{F}_t| \le 2$ under unit lots) (`source-reported`).
- $m_{t+1}$: Post-action mid-price at next decision epoch (`source-reported`).
- $p(f), \Delta q(f)$: Execution price and signed fill quantity (+1 for buy, -1 for sell) (`source-reported`).
- $\varphi$: Inventory risk penalty coefficient ($\varphi = 10^{-3}$ for normal risk, $\varphi = 5 \times 10^{-3}$ for high risk, `source-reported`).
- $q_w = q_{\max}/2 = 4$: Soft inventory wall threshold (`source-reported`).
- $w_{\mathrm{inv}}$: Inventory wall quadratic penalty weight ($w_{\mathrm{inv}} = 5 \times 10^{-2}$, `research-proposed` operational default in codebase).

### Deep Learning Architecture & Hyperparameters
- **Backbone:** Rainbow Distributional DQN (C51) with Dueling streams (`source-reported`).
- **Feature Trunk:** 1 hidden layer with 256 ReLU units (`source-reported`).
- **Distributional Head:** Dueling C51 head over 6 actions, with $N = 101$ categorical atoms uniformly spanning the support $[V_{\min}, V_{\max}] = [-3.0, +3.0]$ (`source-reported`).
- **Target Formulation:** Double DQN with $n=3$ step SMDP returns:
  $$G_t^{(n)} = \sum_{i=0}^{n-1} \gamma^{M_i} r_{t+i} + \gamma^{M_n} \max_{a'} Q_{\theta^-}(s_{t+n}, a')$$
- **Optimization:** AdamW optimizer, initial learning rate $\eta = 3 \times 10^{-4}$, batch size 64 (`source-reported`).
- **Replay Buffer:** Prioritized Experience Replay (PER) of size $|\mathcal{B}| = 10^5$, prioritized by categorical cross-entropy loss (`source-reported`). Target network synchronized every 2,000 gradient steps (`source-reported`).

### Scenario-Bandit Robust Fine-Tuning (Algorithm C)
- Pool of $M = 256$ exogenous regime scenarios (128 random-persistence with $\tau_k \sim \mathrm{Uniform}\{15, 30, 60, 120, 240\}$, 128 correlated-direction with $\rho_{\mathrm{side}} = 0.85$ directional sign persistence, `source-reported`).
- Penalized terminal score: $H_T(\theta; \xi_i) = \mathrm{PnL}_T(\theta; \xi_i) - \sum_{t=0}^{T-1} [ \varphi q_{t+1}^2 + w_{\mathrm{inv}} (|q_{t+1}| - q_w)_+^2 ]$ (`source-reported`).
- Scenario loss: $L_i = -H_T(\theta; \xi_i)$. Scenario difficulty score updated via EMA:
  $$d_i \leftarrow (1 - \alpha_{\mathrm{ema}}) d_i + \alpha_{\mathrm{ema}} L_i$$
  with EMA smoothing factor $\alpha_{\mathrm{ema}} = 0.05$ (`research-proposed` in code, `source-reported` structure).
- Sampling distribution: Standardized difficulty $\nu_i = (d_i - \bar{d}) / (s_d + \epsilon_\nu)$, softmax weights $\widetilde{w}_i \propto \exp(\beta_{\mathrm{sb}} \nu_i)$, mixed with uniform exploration:
  $$p_i = (1 - \varepsilon) \widetilde{w}_i + \varepsilon / M$$
  with per-scenario probability capped at $w_{\max} = 0.05$ (`source-reported`).
- Annealing schedule: $\beta_{\mathrm{sb}}$ annealed from $0.0 \to 0.5$, $\varepsilon$ annealed from $1.0 \to 0.5$ over the first half of fine-tuning; easiest 10% of scenarios refreshed every 500 bandit steps (`source-reported`).

## Required data

- **Market Type:** Central Limit Order Book (continuous double auction, price-time FIFO priority).
- **Timeframe / Resolution:** Tick-by-tick message stream (Level-3 events: limit order placements, market orders, cancellations).
- **Observation Fields:**
  - Best bid price ($B_t$) and best ask price ($A_t$);
  - Bid and ask queue depths at best and one tick deep ($d_{t,0}^b, d_{t,1}^b, d_{t,0}^a, d_{t,1}^a$);
  - Signed market order transaction feed ($y_t \in \{-1, +1\}$) for the Bayesian filter;
  - Agent's own active order queue position ($\mathrm{qa}_t^b, \mathrm{qa}_t^a$) and inventory $q_t$.
- **Source Calibration Data:**
  - LOBSTER Level-3 dataset for AMZN (28 trading days, August 1, 2025 to September 10, 2025).
  - Santa Fe Poisson flow parameters calibrated from AMZN data: LO intensity $\lambda = 0.06$/s/level, MO intensity $2\mu = 0.20$/s ($p_{\mathrm{buy}} = 0.50$ baseline), cancellation rate $\theta_{\mathrm{cxl}} = 0.02$/s/depth (`source-reported`).
  - GLFT benchmark calibration: baseline fill intensity $A = 0.1507$, decay $\kappa = 2.335$, diffusion volatility scale $\sigma = 0.30\,\mathrm{ticks}/\sqrt{\mathrm{s}}$ extracted from the volatility signature plateau (`source-reported`).

## Execution assumptions

- **Quote Sizing:** Fixed unit lot (1 unit lot per quote, maximum 1 resting bid and 1 resting ask active simultaneously) (`source-reported`).
- **Fill Protocol:** Strict FIFO price-time priority inside an event-driven LOB simulator. An active quote fills only when incoming aggressive market orders exhaust all prior resting volume at that price level (`source-reported`).
- **Quote Replacement Cost:** Zero explicit order modification/cancellation fee in simulation (`source-reported`); queue priority is lost upon price alteration, creating endogenous priority penalty (`source-reported`).
- **Exchange Fees & Rebates:** The baseline simulation evaluates gross trading PnL with zero exchange transaction fees (`source-reported`). In realistic production or crypto deployment, maker rebates and taker fees must be explicitly modeled (`research-proposed`).
- **Slippage & Impact:** Limit order fills execute exactly at the quoted limit price (no adverse price slippage on passive fills); market impact is endogenous to the zero-intelligence order book depth (`source-reported`).

## Evidence

### Source-reported

All empirical results below are directly reported by Moret & Lillo (arXiv:2609.11614v1, September 2026):

1. **Stationary Performance (Algorithm A vs. GLFT vs. At-Best):**
   - Paired-seed evaluation over $N_{\mathrm{sim}} = 1000$ episodes of $N_{\mathrm{steps}} = 5000$ LOB events each.
   - GLFT vs. At-Best: Paired Wilcoxon test on per-seed PnL difference $\Delta = \mathrm{PnL}_{\mathrm{GLFT}} - \mathrm{PnL}_{\text{at-best}}$ yields median $\Delta = +0.02$ ($p \approx 0.05$ at $\gamma_{\mathrm{GLFT}} = 10^{-6}$), $\Delta = -0.015$ ($p = 0.008$ at $\gamma_{\mathrm{GLFT}} = 10^{-3}$), and $\Delta = -0.10$ ($p \ll 10^{-4}$ at $\gamma_{\mathrm{GLFT}} = 10^{-1}$). GLFT's primary benefit over at-best is strict inventory containment rather than raw mean PnL.
   - Rainbow DQN (Algorithm A) vs. GLFT: The DQN risk-return frontier strictly dominates GLFT across the entire observed risk range ($\varphi \in [10^{-4}, 10^{-2}]$ vs $\gamma_{\mathrm{GLFT}} \in [10^{-6}, 10^{-1}]$).

2. **Static Asymmetry Misspecification:**
   - When evaluating symmetric-calibrated GLFT under static asymmetric flow ($p_{\mathrm{buy}} \ne 0.50$), GLFT becomes net loss-making once asymmetry exceeds $|p_{\mathrm{buy}} - 0.50| \approx 0.08$.
   - The stationary Rainbow DQN (Algorithm A) remains profitable across a wider envelope $p_{\mathrm{buy}} \in [0.40, 0.60]$, but also transitions to losses under severe asymmetry.

3. **Persistent Regime Degradation:**
   - Under regime-switching flow ($\omega = 0.30$, $p_{\mathrm{buy}} \in [0.20, 0.80]$), sweeping mean regime duration $\tau_r \in \{15, 30, 60, 120, 240\}$ MO events over $N_{\mathrm{sim}} = 100$ paired episodes:
   - Algorithm A terminal PnL decays monotonically from ~+30% of stationary baseline at $\tau_r = 15$ to $-91\%$ at $\tau_r = 240$, becoming severely loss-making due to inventory saturation at $\pm q_{\max} = \pm 8$.

4. **Algorithm B Regime-Aware Recovery:**
   - Over $N_{\mathrm{sim}} = 100$ paired-seed episodes of $N_{\mathrm{steps}} = 100,000$ LOB events at $\tau_r = 60$ MO events, $\omega = 0.30$:
   - Unadapted Algorithm A falls to $-46\%$ of the stationary benchmark.
   - Algorithm B recovers to $+37\%$ of the stationary benchmark, representing a paired recovery of $\approx 80\%$ relative to unadapted Algorithm A.
   - Paired t-test rejects equality with $p < 10^{-4}$.
   - Time-averaged inventory standard deviation: Algorithm A widens to $1.89\times$ the symmetric baseline, whereas Algorithm B contracts to $0.55\times$ the baseline.

5. **Out-of-Distribution Stress Tests (Algorithm B):**
   - Persistence Sweep: Algorithm B remains profitable across all $\tau_r \in [15, 240]$ MO events, declining mildly from ~+46% at $\tau_r = 15$ to ~+23% at $\tau_r = 240$.
   - Random Persistence ($\tau_k \sim \mathrm{Uniform}\{15, 30, 60, 120, 240\}$): Mean terminal PnL drops only 6.9% relative to fixed $\tau_r = 60$ over $N_{\mathrm{sim}} = 50$ episodes of 500,000 events.
   - Correlated Direction ($\rho_{\mathrm{side}} = 0.85$): Mean terminal PnL declines 16.4% relative to fixed $\tau_r = 60$, maintaining positive profitability but exhibiting increased left-tail dispersion.

6. **Algorithm C Scenario-Bandit Fine-Tuning:**
   - Random Persistence Stress: Algorithm C improves mean terminal PnL by ~16% and compresses the empirical PnL standard deviation to ~70% of Algorithm B.
   - Correlated Direction Stress: Algorithm C improves mean terminal PnL by ~17% and compresses standard deviation to ~76% of Algorithm B.

### Independently reproduced

Not independently reproduced. All figures and performance metrics represent third-party reported findings from Moret & Lillo (arXiv:2609.11614v1) and their committed repository code.

### Negative evidence

- **Stationary Quoting Fragility:** Both classical closed-form models (GLFT) and stationarily trained deep RL market makers (Algorithm A) fail decisively under persistent directional order flow, suffering catastrophic drawdowns caused by inventory saturation at $\pm q_{\max}$.
- **Static Asymmetry Sensitivity:** Closed-form GLFT breaks and generates negative PnL under modest static flow imbalance ($|p_{\mathrm{buy}} - 0.50| > 0.08$).
- **Tail Risk Inflation:** Under out-of-distribution random persistence and correlated directional switches, average-case trained policies (Algorithm B) suffer substantial left-tail variance, proving that average-case training is insufficient for worst-case microstructure stability without explicit bandit reweighting.

## Falsification plan

The strategy hypothesis asserts that combining Bayesian online changepoint detection with queue-adjusted exposure signals and scenario-bandit curriculum training enables profitable, inventory-contained market making under non-stationary order flow.

Operational tests to falsify this mechanism:
1. **Regime Duration Stress Test:** Test the controller under heavy-tailed (Pareto-distributed) regime durations with tail index $\alpha < 1.5$ (`research-proposed`).
   - *Failure Rule:* If mean terminal PnL becomes negative across 500 out-of-sample episodes, falsify the exponential-hazard BOCPD assumption (`research-defined falsification threshold`).
2. **Fee & Latency Hurdle Test:** Introduce realistic exchange transaction costs (e.g. 0.01% taker fee, 0.002% maker fee) and a 10–50 ms execution latency delay between decision epoch and order arrival (`research-proposed`).
   - *Failure Rule:* If net PnL turns negative after fees or if fill rate drops by $> 50\%$ due to latency-induced queue displacement, reject the strategy for electronic implementation (`research-defined falsification threshold`).
3. **Inventory Saturation Gate:** In non-stationary flow with $\tau_r \le 120$ MO events and $\omega \le 0.30$:
   - *Failure Rule:* If time spent at the hard inventory boundary $|q_t| = q_{\max}$ exceeds 15% of total episode duration, reject the quote-exposure defense mechanism (`research-defined falsification threshold`).
4. **Adversarial / Strategic Counterparty Test:** Replace the zero-intelligence Santa Fe Poisson flow with an agent-based model featuring predatory traders who detect resting quotes and deliberately front-run or pick off passive limit orders (`research-proposed`).
   - *Failure Rule:* If the agent fails to maintain positive spread capture against strategic execution algorithms, the zero-intelligence simulation premise is falsified (`research-defined falsification threshold`).

## Crypto portability

**Portability Classification:** `adapted/unproven`

The primary source derives and calibrates its methodology on equity Level-3 data (AMZN) within a simulated continuous double auction. It does not provide empirical tests on cryptocurrency markets.

Crypto market adaptation considerations (`research interpretation`):
- **Perpetual Futures Funding Pressure:** Unlike equity markets where order flow mean-reverts on daily horizons, crypto perpetuals exhibit persistent funding-rate-driven directional flows. High positive funding incentives aggressive short market orders, creating prolonged multi-hour directional regimes that severely stress market maker inventory.
- **24/7 Continuous Trading:** Elimination of market open/close boundaries simplifies training but requires continuous real-time BOCPD parameter maintenance without overnight resets.
- **Fee Tier Inversion:** Crypto exchanges (e.g. Binance USD-M, Bybit, Hyperliquid) operate maker-taker fee structures where institutional market makers earn negative maker fees (rebates of 0.5–1.5 bps). If the spread-capture margin in simulation (~0.43 ticks) is narrower than retail taker fees, the strategy is only viable for maker-rebate tiers (`research-proposed`).
- **Cross-Venue Toxic Flow & Latency Arbitrage:** In crypto, price discovery occurs across multiple fragmented centralized and decentralized venues. Aggressive market orders hitting a single venue are frequently toxic arbitrageurs responding to lead-lag signals on external venues. The queue-exposure feature $x_t$ must be augmented with cross-exchange order flow imbalance (`research-proposed`).
- **Liquidation Cascades:** Extreme crypto volatility spikes trigger automated liquidation engines that submit market orders in massive clusters. The BOCPD filter must accommodate jump-diffusion intensity spikes rather than constant Poisson baseline intensities (`research-proposed`).

## Limitations

- **Zero-Intelligence Simulator Limitation:** Order flow is generated by a Santa Fe Poisson model. While calibrated to empirical AMZN Level-3 message data, it neglects strategic counterparties, price-dependent cancelation clustering, and endogenous feedback from the market maker's own quotes on exogenous participants.
- **Unit Lot Restriction:** The agent is restricted to posting at most one unit lot per side. Multi-level quoting (laddering) and inventory-dependent order sizing are not supported by the action space (`source-reported`).
- **Coarse Discrete Quoting Grid:** The 6-action space only permits offsets of $\{-1, 0, +1\}$ ticks relative to touch, preventing deep inventory skewing or multi-tick defensive retreats during extreme volatility spikes (`source-reported`).
- **BOCPD Prior Misspecification:** The Bayesian filter assumes a constant reset hazard $h = 1/\tau_r$ derived from an exponential regime duration prior. If real regime durations follow power-law or clustered Hawkes dynamics, the changepoint probability will be systematically miscalibrated (`research-proposed`).
- **Execution Cost Omission:** The paper omits exchange exchange fees, exchange colocation latency, and API cancellation rate limits, which are material constraints for high-frequency market-making strategies.

## Implementation status

`not-implemented`

No implementation has been built in NautilusTrader, PyBroker, or internal production trading infrastructure. The strategy exists solely as public academic research and standalone Python simulation code.

## Adoption boundary

This document is a research record only. Its presence in this repository does not constitute:
- Validation of alpha in production or crypto markets;
- Approval for live trading, testnet deployment, or paper trading;
- Implementation authorization within execution systems.

Any operational adoption requires independent replication on live venue tick data, integration of exact exchange fee schedules, and explicit multi-agent latency stress testing.

## Related Wiki records

- `[[market-making-axiomatic-unified-inventory-quoting-spread-decomposition-2026-09-02]]`
- `[[multi-level-market-making-logistic-normal-deep-sets-2026-09-02]]`
- `[[sinkhorn-robust-rl-high-frequency-market-making-2026-09-02]]`
- `[[optimal-adaptive-market-making-perpetual-zero-fee-hjb-2026-09-03]]`
- `[[retail-crypto-microstructure-signal-falsification-order-flow-cvd-funding-patterns-2026-09-11]]`

## Sources

1. Felipe Moret and Fabrizio Lillo, *"Deep Learning of Robust Market Making under Regime-Switching Order Flow"*, arXiv preprint `arXiv:2609.11614v1 [q-fin.TR, cs.LG, q-fin.CP]`, submitted September 10, 2026.
   - Stable URL: https://arxiv.org/abs/2609.11614
   - HTML version: https://arxiv.org/html/2609.11614v1
   - PDF version: https://arxiv.org/pdf/2609.11614v1
   - DOI: [10.48550/arXiv.2609.11614](https://doi.org/10.48550/arXiv.2609.11614)
2. Felipe Moret and Fabrizio Lillo, *"robust-deep-market-making"* GitHub repository, commit `395aed7ce98d97684496bc7e3c23a2e64385630a`, September 10, 2026.
   - Repository URL: https://github.com/felipemoret77/robust-deep-market-making
3. Olivier Guéant, Charles-Albert Lehalle, and Joaquin Fernandez-Tapia, *"Dealing with the inventory risk: a solution to the market making problem"*, Mathematics and Financial Economics 7(4): 477–507, 2013. DOI: [10.1007/s11579-012-0087-0](https://doi.org/10.1007/s11579-012-0087-0).
4. Ryan Prescott Adams and David J.C. MacKay, *"Bayesian Online Changepoint Detection"*, arXiv preprint `arXiv:0710.3742 [stat.ML]`, 2007. URL: https://arxiv.org/abs/0710.3742.
5. Matteo Hessel et al., *"Rainbow: Combining Improvements in Deep Reinforcement Learning"*, AAAI Conference on Artificial Intelligence 32(1), 2018. DOI: [10.1609/aaai.v32i1.11796](https://doi.org/10.1609/aaai.v32i1.11796).
