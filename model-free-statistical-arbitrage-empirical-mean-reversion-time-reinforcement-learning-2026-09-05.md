---
schema: strategy-research-record-v1
title: "Model-Free Statistical Arbitrage: Empirical Mean Reversion Time Minimization and Simulation-Trained Reinforcement Learning Policy"
created: 2026-09-05
updated: 2026-09-05
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - statistical-arbitrage
  - pairs-trading
  - reinforcement-learning
  - q-learning
  - empirical-mean-reversion-time
  - sim2real
  - equities
status: research-only
confidence: high
source_as_of: 2024-03-18
sources:
  - "Boming Ning and Kiseop Lee, 'Advanced Statistical Arbitrage with Reinforcement Learning', arXiv:2403.12180v1 [q-fin.ST], March 18, 2024. https://arxiv.org/abs/2403.12180"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Model-Free Statistical Arbitrage: Empirical Mean Reversion Time Minimization and Simulation-Trained Reinforcement Learning Policy

## Provenance

- **Primary Academic Source:** Boming Ning (Department of Statistics, Purdue University, West Lafayette, IN 47907, USA; `ningb@purdue.edu`, corresponding author) and Kiseop Lee (Department of Statistics, Purdue University, West Lafayette, IN 47907, USA), *"Advanced Statistical Arbitrage with Reinforcement Learning"*, arXiv preprint `arXiv:2403.12180v1 [q-fin.ST]`, submitted March 18, 2024.
  - Canonical arXiv Abstract: [https://arxiv.org/abs/2403.12180](https://arxiv.org/abs/2403.12180)
  - Canonical DOI: [https://doi.org/10.48550/arXiv.2403.12180](https://doi.org/10.48550/arXiv.2403.12180)
  - Full-Text HTML: [https://arxiv.org/html/2403.12180v1](https://arxiv.org/html/2403.12180v1)
  - Primary LaTeX Package: `https://arxiv.org/src/2403.12180` (audited directly from unpacked source files `main.tex`, figures, and empirical tables).
- **Associated Code / Implementation Verification:** The paper does not link a public GitHub repository in the text; data was sourced via public Yahoo Finance API (`yfinance`). All mathematical definitions, stopping-time algorithms, state-space equations, and empirical tables were directly audited and verified from the primary LaTeX source package.
- **Pre-Write Deduplication & Identity Verification:** An exhaustive scan across all 378 markdown strategy records in `alpha-strategy-research` confirmed zero existing records matching `2403.12180`, `Boming Ning`, `Kiseop Lee`, or `empirical mean reversion time` / `EMRT`. Existing statistical arbitrage records in the repository focus on autoencoder policy learning (`end-to-end-statistical-arbitrage-autoencoder-policy-2026-09-05.md`), graph clustering on correlation networks (`graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05.md`), convex-concave programming (`moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05.md`), graphical matching (`graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05.md`), and deep learning factor replication (`statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05.md`). None of the existing records utilize non-parametric empirical mean-reversion time minimization based on Fink-Gandhi extrema or simulation-to-reality (Sim2Real) reinforcement learning policies for statistical arbitrage execution.

## Economic mechanism

### Source-reported

1. **Failure of Classical Parametric Assumptions:** Classical pairs trading and statistical arbitrage frameworks rely on strong parametric assumptions. In distance methods (Gatev et al., 2006), pairs are formed by minimizing sum of squared deviations (SSD) and traded via static standard-deviation bands ($\pm 2\sigma$). In continuous-time stochastic spread methods (Avellaneda & Lee, 2010; Leung & Li, 2015, 2016), spreads are assumed to strictly follow an Ornstein-Uhlenbeck (OU) process ($dX_t = \mu(\theta - X_t)dt + \sigma dW_t$), with parameters $(\mu, \theta, \sigma)$ estimated via Maximum Likelihood Estimation (MLE). However, real financial market spreads frequently violate Gaussianity, exhibit time-varying volatility clustering, and experience structural parameter drift between the formation period and the trading period.
2. **Empirical Mean Reversion Time (EMRT) as a Model-Free Metric:** The authors demonstrate that in mean-reverting processes, the mean-reversion speed parameter $\mu$ is the primary determinant of strategy profitability, where higher $\mu$ yields faster convergence and higher annualized returns. To eliminate parametric distribution assumptions, the authors define an empirical reversion time metric $r$ based on the time intervals between significant local extremes (Fink & Gandhi, 2007) and crossings of the sample mean $\hat{\theta}$. Minimizing this empirical reversion time via a grid search directly selects asset hedge ratios that maximize the physical speed of mean reversion without requiring Gaussian or Markovian assumptions.
3. **Dynamic Adaptation via Reinforcement Learning:** Fixed deviation thresholds (e.g., entering at $k \cdot \sigma$) suffer from rigid hyperparameter tuning that degrades out of sample. By reformulating trade execution as a Markov Decision Process (MDP), a reinforcement learning agent learns dynamic state-to-action policies based on recent directional price trajectories ($S_t$) rather than historical static variance bands. 
4. **Simulation-to-Reality (Sim2Real) Transfer:** In real markets, a trader observes only a single historical realization of spread prices, making RL agents prone to severe overfitting. Furthermore, the true equilibrium mean $\theta$ is unobservable. To solve this, the authors train the Q-learning agent across 10,000 synthetic OU paths where the true equilibrium mean is known and rewarded, establishing a generalized mean-reversion execution policy that transfers zero-shot to real-market equity spreads.

### Research interpretation

1. **Velocity-Maximizing Cointegration Filter:** EMRT functions as a non-parametric proxy for the half-life of mean reversion ($t_{1/2} = \ln(2)/\mu$). Traditional Engle-Granger or Johansen cointegration tests optimize stationarity or t-statistics, which can select pairs that are mathematically stationary but exhibit multi-month mean-reversion cycles with high capital drag. EMRT directly penalizes long excursion durations, preferentially selecting pairs that cross their equilibrium frequently.
2. **Path-Dependent Microstructure Memory:** By quantizing the past $l$ price steps into directional states, the RL agent conditions on local momentum vs. exhaustion dynamics. Traditional z-score strategies trigger mechanically at extreme deviations, frequently catching falling knives during structural breaks; an RL agent trained on path dynamics learns to delay entry until deceleration signals appear.
3. **Sim2Real Transfer Gap and Overfitting Mitigation:** The sim2real approach acts as a structural regularizer: because the agent is trained only on canonical mean-reverting synthetic paths, it cannot overfit to idiosyncratic equity noise in historical sample data. However, this creates a model mismatch: real spreads contain jump risk, non-stationary trends, and fat-tailed shocks absent in standard Ornstein-Uhlenbeck simulations.

## Signal

The strategy operates in two distinct phases: (1) an annual formation phase that constructs the optimal mean-reverting spread via EMRT minimization, and (2) an execution phase driven by a simulation-trained Q-learning reinforcement learning policy.

### 1. Spread Construction via Empirical Mean Reversion Time (`source-reported`)

Over a historical formation window $[t-h, t]$ (1 calendar year, 252 trading days; `source-reported`):
1. **Asset Pair Selection:** Identify candidate pairs of economically related stocks $(S_1, S_2)$ within sector universes (`source-reported`).
2. **Spread Formulation:** Form the two-asset linear spread:
   $$X_t = S_{1,t} - B \cdot S_{2,t} \quad (\text{source-reported})$$
   where the first asset's weight is normalized to $a_1 = 1$ without loss of generality (`source-reported`).
3. **Important Extrema Identification (Fink & Gandhi 2007; `source-reported`):**
   - Let $s$ be the sample standard deviation of candidate spread $X_t$ over the formation window (`source-reported`).
   - Let $C$ be a positive threshold parameter (fixed at $C = 2.0$; `source-reported`).
   - A discrete point $X_m$ is an *important minimum* if there exist indices $i \leq m \leq j$ such that:
     $$X_m = \min(X_i, \dots, X_j) \quad \text{and} \quad X_i - X_m \geq C \cdot s, \quad X_j - X_m \geq C \cdot s \quad (\text{source-reported})$$
   - A discrete point $X_m$ is an *important maximum* if there exist indices $i \leq m \leq j$ such that:
     $$X_m = \max(X_i, \dots, X_j) \quad \text{and} \quad X_m - X_i \geq C \cdot s, \quad X_m - X_j \geq C \cdot s \quad (\text{source-reported})$$
4. **Stopping-Time Moments Sequence $\{\tau_n\}_{n=1}^N$ (`source-reported`):**
   - Let $\hat{\theta} = \bar{X}$ denote the sample mean of the spread over $[0, T]$ (`source-reported`).
   - The sequence of stopping times is generated recursively:
     $$\tau_1 = \inf \{u \in [0, T] : X_u \text{ is a local extreme}\} \quad (\text{source-reported})$$
     $$\tau_2 = \inf \{u \in [\tau_1, T] : X_u = \hat{\theta}\} \quad (\text{source-reported})$$
     $$\tau_3 = \inf \{u \in [\tau_2, T] : X_u \text{ is a local extreme}\} \quad (\text{source-reported})$$
     $$\tau_4 = \inf \{u \in [\tau_3, T] : X_u = \hat{\theta}\} \quad (\text{source-reported})$$
   - In general:
     - Odd moments $\tau_n$ ($n = 1, 3, 5, \dots$) represent occurrences of significant local extrema (`source-reported`).
     - Even moments $\tau_n$ ($n = 2, 4, 6, \dots$) represent subsequent crossings of the sample mean $\hat{\theta}$ (`source-reported`).
5. **Empirical Mean Reversion Time (EMRT) Metric $r$ (`source-reported`):**
   $$r = \frac{2}{N} \sum_{\substack{i=2 \\ i \text{ even}}}^N (\tau_i - \tau_{i-1}) \quad (\text{source-reported})$$
   representing the average duration required for the spread to revert to its mean from an important local extreme (`source-reported`).
6. **Grid Search Optimization (`source-reported`):**
   - Perform a discrete grid search over $B \in [-3.00, 3.00]$ with step size $0.01$ (i.e., $B \in \{-3.00, -2.99, \dots, 2.99, 3.00\}$; `source-reported`).
   - Select the optimal coefficient $B^*$ that minimizes $r$, subject to the sample variance bound $S^2(X) < M$ to prevent excessive leverage (`source-reported`).

### 2. Reinforcement Learning Execution Policy (`source-reported`)

#### A. Synthetic Pre-Training Environment (`source-reported`)
- **Simulation Process:** Simulate 10,000 sample paths of a stationary Ornstein-Uhlenbeck process:
  $$dX_t = \mu(\theta - X_t)dt + \sigma dW_t \quad (\text{source-reported})$$
  with fixed parameters $\mu = 1.0$, $\theta = 1.0$, $\sigma = 0.1$, terminal time $T = 252$ steps, $n = 252$ points (`source-reported`).
- **State Space Construction:**
  - Given a lookback window of length $l$ (set to $l = 4$; `source-reported`).
  - Compute daily percentage price changes: $\pi_i = \left(\frac{P_i - P_{i-1}}{P_{i-1}}\right) \times 100$ for $i \in [t - l + 1, t]$ (`source-reported`).
  - In Section 4.2 of the paper, price changes are quantized into 4 discrete levels using threshold $k$ (e.g., $k = 3\%$):
    $$d_i = \begin{cases} +2 & \text{if } \pi_i > k \\ +1 & \text{if } 0 < \pi_i < k \\ -1 & \text{if } -k < \pi_i < 0 \\ -2 & \text{if } \pi_i < -k \end{cases} \quad (\text{source-reported})$$
  - State vector: $S_t = [d_{t-l+1}, d_{t-l+2}, \dots, d_t]$ (`source-reported`).
  - *Provenance Note:* Section 4.2 describes $4^l$ unique states ($4^4 = 256$), whereas Section 5.2 states $l = 4$ generated 16 distinct states ($2^4 = 16$). This indicates that the empirical implementation binarized changes into positive and negative signs ($d_i \in \{+1, -1\}$; `research-identified provenance gap`).
- **Action Space:**
  - $A_t \in \{-1, 0, +1\}$ (`source-reported`):
    - When flat ($I_t = 0$): Allowed actions are Buy ($A_t = +1$) or Hold ($A_t = 0$) (`source-reported`).
    - When long ($I_t = +1$): Allowed actions are Sell ($A_t = -1$) or Hold ($A_t = 0$) (`source-reported`).
    - *Asymmetry:* The strategy is strictly long-only on the spread (does not initiate short positions on the spread; `source-reported`).
- **Reward Function:**
  $$R_{t+1} = A_t \cdot (\theta - X_t) - c \cdot |A_t| \quad (\text{source-reported})$$
  where $\theta$ is the true global equilibrium mean, $X_t$ is current spread price, and $c$ is transaction cost per trade (`source-reported`).
  - If $X_t < \theta$ (spread undervalued): Buy ($A_t = +1$) receives positive reward $(\theta - X_t) > 0$; Sell receives negative reward.
  - If $X_t > \theta$ (spread overvalued): Sell ($A_t = -1$) receives positive reward $-(\theta - X_t) > 0$; Buy receives negative reward.
- **Q-Learning Update:**
  $$Q^{\text{new}}(S_t, A_t) = Q(S_t, A_t) + \alpha \left[ R_{t+1} + \gamma \max_a Q(S_{t+1}, a) - Q(S_t, A_t) \right] \quad (\text{source-reported})$$
  Hyperparameters: learning rate $\alpha = 0.1$, discount factor $\gamma = 0.99$, exploration $\epsilon = 0.1$, trained over 10 episodes (`source-reported`).

#### B. Real-World Execution Protocol (`source-reported`)
- **Action Selection:** Evaluate the pre-trained Q-table with exploitation parameter $\epsilon = 0$ (greedy action selection based on $\argmax_a Q(S_t, a)$; `source-reported`).
- **Order Timing & Sizing:**
  - Evaluate state $S_t$ at daily close (`source-reported`).
  - Sizing rule: At each buy signal, 100% of available portfolio cash is committed to buying the spread ($+1$ share of $S_1$ and $-B^*$ shares of $S_2$; `source-reported`).
  - Position is held until the RL agent outputs a sell signal ($A_t = -1$), which closes the entire spread position (`source-reported`).
  - Next-bar market execution at market open / close (`research-proposed fill assumption`; paper evaluates daily closing series).

## Required data

- **Instrument / Universe:**
  - 10 representative US equity pairs across 10 sectors of the S&P 500 (`source-reported`):
    1. Technology: MSFT (Microsoft) - GOOGL (Alphabet)
    2. Healthcare: CVS (CVS Health) - JNJ (Johnson & Johnson)
    3. Consumer Goods: CL (Colgate-Palmolive) - KMB (Kimberly-Clark)
    4. Financials: V (Visa) - MA (Mastercard)
    5. Industrials: GE (General Electric) - BA (Boeing)
    6. Energy: OXY (Occidental Petroleum) - XOM (ExxonMobil)
    7. Real Estate: WELL (Welltower) - VTR (Ventas)
    8. Materials: PPG (PPG Industries) - SHW (Sherwin-Williams)
    9. Telecommunication: VZ (Verizon) - TMUS (T-Mobile US)
    10. Transportation: CSX (CSX Corp) - NSC (Norfolk Southern)
- **Timeframe & Resolution:** Daily adjusted closing prices (`source-reported`).
- **Data Source & History:** Yahoo Finance API (`yfinance`; `source-reported`).
  - Formation window: 2022-01-01 to 2022-12-31 (252 trading days; `source-reported`).
  - Out-of-sample trading window: 2023-01-01 to 2023-12-31 (252 trading days; `source-reported`).
- **Fields:** Daily adjusted closing prices (accounting for splits and dividends; `source-reported`).
- **Point-in-Time Hygiene:** Historical formation strictly precedes the trading phase; no look-ahead in Q-table lookup (`source-reported`).

## Execution assumptions

- **Order Types & Timing:** Daily close rebalancing / next-day open execution (`research-proposed`; paper assumes execution on daily adjusted closing prices).
- **Position Sizing & Capital Reinvestment:**
  - Initial capital: $100 allocated per pair (`source-reported`).
  - Sizing: All available cash is deployed on each buy signal (100% cash reinvestment; `source-reported`).
  - No simultaneous multi-tier sizing; position is binary (0 or 100% long spread; `source-reported`).
- **Transaction Costs & Slippage:**
  - The theoretical reward function defines cost penalty $c \cdot |A_t|$ (`source-reported`).
  - However, in the empirical backtest (Tables 3 & 4), transaction costs are set to $c = 0$ or omitted from explicit deduction (`research-identified provenance gap`).
  - For operational replication, assume $5\text{ bps}$ per leg equity commission and $2\text{ bps}$ half-spread (`research-proposed`).
- **Borrow & Shorting:** Shorting the second stock ($-B^* \cdot S_2$) requires locate and margin borrow availability (`research-proposed`).
- **Margin / Leverage Constraint:** Upper bound $M$ on sample variance $S^2(X) < M$ is imposed to prevent excessive leverage during grid search (`source-reported`).

## Evidence

### Source-reported

#### 1. Simulation Validation of Empirical Mean Reversion Time (Table 1; `source-reported`)
Simulated 100 paths of Ornstein-Uhlenbeck process with $\theta = 0$, $\sigma = 1.0$, $T = 1.0$, $n = 1000$ points, extremum threshold $C = 2.0$, varying $\mu \in [2.0, 20.0]$:

| Mean Reversion Speed $\mu$ | Average EMRT $r$ (steps) | Mean Reversion Speed $\mu$ | Average EMRT $r$ (steps) |
| :--- | :--- | :--- | :--- |
| **2.0** | 98.79 | **12.0** | 49.22 |
| **4.0** | 83.45 | **14.0** | 45.10 |
| **6.0** | 78.09 | **16.0** | 38.04 |
| **8.0** | 59.22 | **18.0** | 35.63 |
| **10.0** | 58.51 | **20.0** | 31.15 |

*Finding:* Confirms strict monotonic inverse relationship between the theoretical mean-reversion speed $\mu$ and empirical mean reversion time $r$ (`source-reported`).

#### 2. Synthetic Simulation RL Trading Performance (`source-reported`)
- Evaluated on 100 newly generated out-of-sample OU paths ($T = 252$, $n = 252$, $\mu = 1.0$, $\theta = 1.0$, $\sigma = 0.1$, initial wealth $100).
- Average cumulative profit across 100 paths exceeded **600%** under full-cash reinvestment (`source-reported`).

#### 3. Calibrated Pairs Trading Coefficients $B$ (Table 2; `source-reported`)
Comparison of hedge ratios derived during 2022 formation period across Distance Method (DM; fixed $B=1.0$), Ornstein-Uhlenbeck MLE (OU), and Empirical Mean Reversion Time (EMRT):

| Pair Index | Sector | DM ($B$) | OU MLE ($B$) | EMRT ($B^*$) |
| :--- | :--- | :--- | :--- | :--- |
| **MSFT-GOOGL** | Technology | 1.0 | 0.99 | 0.89 |
| **CVS-JNJ** | Healthcare | 1.0 | 0.43 | -0.24 |
| **CL-KMB** | Consumer Goods | 1.0 | 0.39 | 0.46 |
| **V-MA** | Financials | 1.0 | 0.53 | 0.33 |
| **GE-BA** | Industrials | 1.0 | 0.20 | 0.34 |
| **OXY-XOM** | Energy | 1.0 | 0.77 | 0.22 |
| **WELL-VTR** | Real Estate | 1.0 | 0.99 | 0.98 |
| **PPG-SHW** | Materials | 1.0 | 0.33 | 0.12 |
| **VZ-TMUS** | Telecommunication | 1.0 | 0.10 | 0.01 |
| **CSX-NSC** | Transportation | 1.0 | 0.12 | 0.14 |

*Provenance Note:* For CVS-JNJ, EMRT grid search selected $B^* = -0.24$. Because the spread is defined as $X = S_1 - B S_2$, this produced $X = \text{CVS} + 0.24\text{JNJ}$, representing a net long position in both assets rather than a market-neutral spread (`research-identified anomaly`).

#### 4. Out-of-Sample Trading Performance on S&P 500 Pairs (Tables 3 & 4; 2023; `source-reported`)

##### Pairs 1–5 (Table 3; `source-reported`):
- **MSFT-GOOGL:**
  - DM: DailyRet 0.0446%, DailyStd 0.4670%, DailySR 0.0955, MaxDD -2.1344%, CumulPnL +11.4443%
  - OU: DailyRet 0.0327%, DailyStd 0.4285%, DailySR 0.0764, MaxDD -2.1427%, CumulPnL +8.2443%
  - **RL:** DailyRet **0.1344%**, DailyStd 1.0754%, DailySR **0.1250**, MaxDD **0.0000%**, CumulPnL **+37.7555%**
- **CVS-JNJ:**
  - DM: DailyRet 0.0440%, DailyStd 2.0692%, DailySR 0.0213, MaxDD -24.6778%, CumulPnL +5.7581%
  - OU: DailyRet -0.0073%, DailyStd 1.4950%, DailySR -0.0049, MaxDD -25.6665%, CumulPnL -4.5179%
  - **RL:** DailyRet **0.0585%**, DailyStd 0.7506%, DailySR **0.0780**, MaxDD **0.0000%**, CumulPnL **+14.8895%**
- **CL-KMB:**
  - DM: DailyRet 0.0659%, DailyStd 1.2314%, DailySR 0.0535, MaxDD -13.6791%, CumulPnL +15.6385%
  - OU: DailyRet 0.0198%, DailyStd 0.7589%, DailySR 0.0261, MaxDD -5.7253%, CumulPnL +4.298%
  - **RL:** DailyRet **0.0826%**, DailyStd 0.6000%, DailySR **0.1377**, MaxDD **-1.9476%**, CumulPnL **+22.2879%**
- **V-MA:**
  - DM: DailyRet -0.0244%, DailyStd 1.1796%, DailySR -0.0207, MaxDD -10.7238%, CumulPnL -7.4888%
  - OU: DailyRet 0.0342%, DailyStd 0.3475%, DailySR 0.0985, MaxDD -1.0185%, CumulPnL +8.7348%
  - **RL:** DailyRet **0.0330%**, DailyStd 0.3144%, DailySR **0.1049**, MaxDD **-0.6211%**, CumulPnL **+8.4248%**
- **GE-BA:**
  - DM: DailyRet 0.2771%, DailyStd 3.9356%, DailySR 0.0704, MaxDD -18.1823%, CumulPnL +64.2387%
  - OU: DailyRet 0.0392%, DailyStd 0.3890%, DailySR 0.1007, MaxDD 0.0000%, CumulPnL +10.046%
  - **RL:** DailyRet **0.1679%**, DailyStd 1.2803%, DailySR **0.1312**, MaxDD **0.0000%**, CumulPnL **+48.8196%**

##### Pairs 6–10 (Table 4; `source-reported`):
- **OXY-XOM:**
  - DM: DailyRet 0.0373%, DailyStd 2.0950%, DailySR 0.0178, MaxDD -19.1535%, CumulPnL +3.9194%
  - OU: DailyRet 0.0238%, DailyStd 1.6012%, DailySR 0.0149, MaxDD -14.5001%, CumulPnL +2.7812%
  - **RL:** DailyRet **0.0609%**, DailyStd 0.9446%, DailySR **0.0861**, MaxDD **-2.0008%**, CumulPnL **+15.0791%**
- **WELL-VTR:**
  - DM: DailyRet 0.0694%, DailyStd 0.6555%, DailySR 0.1058, MaxDD -1.4004%, CumulPnL +18.2114%
  - OU: DailyRet 0.0539%, DailyStd 0.5480%, DailySR 0.0983, MaxDD -1.3798%, CumulPnL +13.9245%
  - **RL:** DailyRet **0.0745%**, DailyStd 0.6794%, DailySR **0.1097**, MaxDD **-3.2895%**, CumulPnL **+19.6910%**
- **PPG-SHW:**
  - DM: DailyRet -0.0772%, DailyStd 1.0113%, DailySR -0.0764, MaxDD -19.1196%, CumulPnL -18.5547%
  - OU: DailyRet 0.0000%, DailyStd 0.0000%, DailySR 0.0000, MaxDD 0.0000%, CumulPnL 0.0000% (no trades triggered)
  - **RL:** DailyRet **0.1124%**, DailyStd 1.0600%, DailySR **0.1061**, MaxDD **0.0000%**, CumulPnL **+30.4559%**
- **VZ-TMUS:**
  - DM: DailyRet -0.1120%, DailyStd 3.7311%, DailySR -0.0300, MaxDD -37.4779%, CumulPnL -36.1756%
  - OU: DailyRet -0.0123%, DailyStd 1.3241%, DailySR -0.0093, MaxDD -18.6520%, CumulPnL -5.0869%
  - **RL:** DailyRet **0.0412%**, DailyStd 0.8037%, DailySR **0.0513**, MaxDD **-3.7306%**, CumulPnL **+9.9163%**
- **CSX-NSC:**
  - DM: DailyRet 0.0000%, DailyStd 0.0000%, DailySR 0.0000, MaxDD 0.0000%, CumulPnL 0.0000% (no trades triggered)
  - OU: DailyRet 0.0199%, DailyStd 0.2879%, DailySR 0.0693, MaxDD 0.0000%, CumulPnL +4.9825%
  - **RL:** DailyRet **0.0496%**, DailyStd 0.7101%, DailySR **0.0698**, MaxDD **0.0000%**, CumulPnL **+12.4263%**

### Independently reproduced

- Not independently reproduced.

### Negative evidence

1. **Transaction Cost Vulnerability:** The empirical backtest results reflect zero explicit commission or slippage deductions. Because pairs trading involves simultaneously maintaining long and short positions across two underlying equities with daily rebalancing, small gross edges (e.g., V-MA daily return $0.0330\% \approx 3.3\text{ bps}$ or VZ-TMUS daily return $0.0412\% \approx 4.1\text{ bps}$) could be substantially degraded or inverted by standard institutional trading frictions ($5\text{--}10\text{ bps}$ round-trip).
2. **Unconstrained Negative Hedge Ratios:** The grid search allowed $B \in [-3.00, 3.00]$, causing CVS-JNJ to receive $B^* = -0.24$. This converted the spread into $X = \text{CVS} + 0.24\text{JNJ}$, eliminating the market-neutral hedge and leaving the position exposed to directional beta risk.
3. **Severe Asymmetry from Long-Only Constraint:** The agent's action space does not permit opening short spread positions when $X_t > \theta$. In classical statistical arbitrage, short-spread trades contribute roughly half of the total strategy alpha. Omitting shorting discards significant capacity and creates a structural long bias.
4. **Single-Regime Out-of-Sample Window:** The empirical evaluation covers only calendar year 2023, an exceptional equity recovery year (S&P 500 up >24%). Performance during sustained bear regimes (such as 2022) or severe liquidity shocks was not evaluated out of sample.

## Falsification plan

To falsify the hypothesis that EMRT-based spread construction and Sim2Real Q-learning generate genuine statistical arbitrage alpha:

1. **Cost Hurdle Stress Test:**
   - Run the 10-pair execution simulation with realistic equity transaction costs: $5\text{ bps}$ per trade commission plus half-spread slippage ($2\text{ bps}$).
   - *Falsification Condition:* If net annualized Sharpe ratio drops below $0.50$ or net cumulative PnL turns negative on $\geq 5$ of the 10 pairs (`research-defined falsification threshold`), reject the claim of cost-viable real-world alpha.
2. **Spread Construction Ablation (EMRT vs. OLS / Johansen Cointegration):**
   - Trade the identical Sim2Real Q-learning policy on spreads formed via standard Engle-Granger OLS cointegration versus spreads formed via EMRT minimization.
   - *Falsification Condition:* If EMRT-formed spreads do not achieve a statistically significant higher mean daily Sharpe ratio or faster mean-reversion cycle than Engle-Granger OLS at the 95% confidence level ($p > 0.05$; `research-defined falsification threshold`), reject the hypothesis that EMRT provides superior spread construction over classical cointegration.
3. **Sim2Real Policy vs. Simple Threshold Baseline Ablation:**
   - Compare the simulation-trained Q-table against a simple dynamic z-score threshold (enter at $z < -1.5$, exit at $z > 0$) on the same EMRT spreads.
   - *Falsification Condition:* If the Q-learning policy fails to outperform the fixed-threshold rule by at least $15\%$ in net risk-adjusted return (`research-defined falsification threshold`), conclude that the reinforcement learning policy adds complexity without meaningful decision edge.
4. **Full Historical Cycle & Regime Breakdown (2018–2024):**
   - Extend the out-of-sample testing across multiple distinct macro regimes, specifically 2018 (Q4 volatility shock), 2020 (COVID liquidity crash), and 2022 (aggressive rate hiking and bear market).
   - *Falsification Condition:* If maximum drawdown exceeds $25\%$ or annualized return falls below 0% during bear market regimes (`research-defined falsification threshold`), reject the claim of regime-invariant statistical arbitrage robustness.

## Crypto portability

- **Portability Classification:** `adapted` / `unproven`.
- **Structural Portability Differences:**
  1. **Cross-Exchange vs. Single-Venue Arbitrage:** In US equities, consolidated tape (SIP) ensures unified pricing across exchanges. In crypto, pairs trading across tokens (e.g., SOL/USDT vs. ETH/USDT or AVAX/USDT vs. SOL/USDT) or between perpetual futures venues (Binance vs. Bybit vs. OKX) faces funding rate divergence and venue-specific liquidation mechanics.
  2. **Funding Rate Drag:** In crypto perpetual futures, holding a synthetic spread $S_1 - B S_2$ incurs 8-hour funding payments on both legs. If the long asset has positive funding (paying longs) and the short asset has negative funding (paying shorts), the net funding drag can rapidly consume the small statistical edge.
  3. **24/7 Continuous Trading & Volatility Scaling:** Equity daily closing discretization ignores overnight gaps and weekend moves. In 24/7 crypto markets, sampling at hourly or 15-minute intervals is required, requiring re-estimation of the EMRT extremum parameter $C$ and lookback window $l$.
  4. **Fat-Tailed Shocks & Breakdowns:** Crypto token correlations frequently decouple catastrophically during protocol exploits, token unlock events, or regulatory actions, rendering historical mean reversion invalid. Stop-loss mechanisms (omitted in Ning & Lee) are mandatory in crypto.

## Limitations

1. **State Space Dimension Discrepancy:** The methodology text (Section 4.2) specifies a 4-level quantization resulting in $4^l = 4^4 = 256$ states, but the experimental implementation (Section 5.2) reports 16 states for $l=4$ ($2^4 = 16$). This indicates an undocumented simplification to binary sign transitions in the actual code (`research-identified provenance gap`).
2. **Long-Only Spread Restriction:** By construction, the policy never shorts overvalued spreads ($A_t \in \{0, +1\}$ when flat), discarding roughly 50% of classical pairs trading alpha and introducing an unhedged beta bias.
3. **Transaction Cost Omission in Backtests:** Reported empirical returns in Tables 3 and 4 omit realistic fees and slippage, overstating net Sharpe ratios for low-margin pairs.
4. **Discretionary Pair Universe:** The 10 sector pairs were selected manually based on subjective similarity rather than an algorithmic cross-sectional screen, creating lookback and selection bias.
5. **No Independent Reproduction:** Results reflect solely the authors' published preprint findings without public repository reproduction.

## Implementation status

- **Current Status:** `not-implemented`.
- No prototype, backtest, or live trading implementation of EMRT grid search or Sim2Real Q-learning exists within this repository or associated execution pipelines (`nautilus-quant-system`).

## Adoption boundary

- **Status:** `research-only`.
- **Adoption:** `not-approved`.
- **Scope:** Research documentation only.
- This capture is an evaluation of an external academic hypothesis and does not authorize capital deployment, live trading, paper trading, or production implementation.

## Related Wiki records

- `[[quant/graphical-matching-pairs-trading-maximum-weight-matching-2026-09-05]]` — Maximum weight matching pairs selection eliminating shared-asset covariance.
- `[[quant/graph-clustering-sponge-ensemble-signal-quality-statistical-arbitrage-2026-09-05]]` — Signed graph clustering on correlation networks for multi-pair statistical arbitrage.
- `[[quant/moving-band-statistical-arbitrage-convex-concave-markowitz-2026-09-05]]` — Convex-concave programming and Markowitz optimization for moving band statistical arbitrage.
- `[[quant/end-to-end-statistical-arbitrage-autoencoder-policy-2026-09-05]]` — End-to-end autoencoder policy learning for multi-asset statistical arbitrage.
- `[[quant/statistical-arbitrage-deep-learning-lstm-factor-replication-ornstein-uhlenbeck-2026-09-05]]` — Deep learning LSTM factor replication for synthetic Ornstein-Uhlenbeck asset pricing.
- `[[quant/crypto-pairs-trading-copula-cointegration-2026-08-31]]` — Non-linear dependency modeling via copulas for cryptocurrency pairs trading.

## Sources

1. **Primary Source:** Boming Ning and Kiseop Lee, *"Advanced Statistical Arbitrage with Reinforcement Learning"*, arXiv preprint `arXiv:2403.12180v1 [q-fin.ST]`, submitted March 18, 2024.
   - Abstract & Metadata: [https://arxiv.org/abs/2403.12180](https://arxiv.org/abs/2403.12180)
   - DOI: [https://doi.org/10.48550/arXiv.2403.12180](https://doi.org/10.48550/arXiv.2403.12180)
   - HTML Full Text: [https://arxiv.org/html/2403.12180v1](https://arxiv.org/html/2403.12180v1)
   - Unpacked Source Archive: `https://arxiv.org/src/2403.12180` (`main.tex`, tables, figures, bibliography).
2. **Supporting Reference (Extrema Detection):** Eugene Fink and Harith Suman Gandhi, *"Important extrema of time series"*, Technical Report, 2007.
3. **Supporting Reference (Baseline Method 1):** Evan Gatev, William N. Goetzmann, and K. Geert Rouwenhorst, *"Pairs trading: Performance of a relative-value arbitrage rule"*, *Review of Financial Studies*, 19(3):797–827, 2006.
4. **Supporting Reference (Baseline Method 2):** Marco Avellaneda and Jeong-Hyun Lee, *"Statistical arbitrage in the US equities market"*, *Quantitative Finance*, 10(7):761–782, 2010.
5. **Supporting Reference (OU Theory):** Tim Leung and Xin Li, *"Optimal Mean Reversion Trading: Mathematical Analysis and Practical Applications"*, Modern Trends in Financial Engineering, World Scientific Publishing Company, 2016.
