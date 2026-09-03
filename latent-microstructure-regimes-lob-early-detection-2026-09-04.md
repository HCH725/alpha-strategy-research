---
schema: strategy-research-record-v1
title: "Latent Microstructure Regimes in Limit Order Books: Causal Three-State Identification and MAX-Fusion Rising-Edge Early Warning Detection"
created: 2026-09-04
updated: 2026-09-04
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - limit-order-book
  - early-warning
  - regime-detection
  - crypto
  - bitcoin
  - high-frequency
  - hmm
  - liquidity-risk
status: research-only
confidence: medium
source_as_of: 2026-08-24
sources:
  - "Prakul Sunil Hiremath and Vruksha Arun Hiremath, 'Early Detection of Latent Microstructure Regimes in Limit Order Books', arXiv preprint arXiv:2604.20949v1 [cs.LG, q-fin.TR, stat.ME], submitted April 24, 2026; revised August 24, 2026. https://arxiv.org/abs/2604.20949"
  - "Prakul Sunil Hiremath and Vruksha Arun Hiremath, 'Early Detection of Latent Micro-Regimes in Limit Order Books', Zenodo Archive, DOI: 10.5281/zenodo.19697687, August 2026. https://doi.org/10.5281/zenodo.19697687"
  - "Prakul Sunil Hiremath, 'LOB-Latent-Regimes: Latent Micro-Regimes in Limit Order Books: Identification and Early Detection', GitHub repository, commit 6bf8ec92632a1f0fd4d4be502d30ad7f2a7007ae, file path Experiments/v7.py, August 2026. https://github.com/prakulhiremath/LOB-Latent-Regimes"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Latent Microstructure Regimes in Limit Order Books: Causal Three-State Identification and MAX-Fusion Rising-Edge Early Warning Detection

## Provenance

- **Primary Paper:** Prakul Sunil Hiremath (Visvesvaraya Technological University, Department of Computer Science and Engineering) and Vruksha Arun Hiremath (K.L.E. Society's College of Business Administration), *"Early Detection of Latent Microstructure Regimes in Limit Order Books"*, arXiv preprint `arXiv:2604.20949v1 [cs.LG, q-fin.TR, stat.ME]`, submitted April 24, 2026; revised August 24, 2026.
- **Canonical arXiv URL:** https://arxiv.org/abs/2604.20949
- **Full Text HTML:** https://arxiv.org/html/2604.20949v1
- **Zenodo Archive DOI:** [10.5281/zenodo.19697687](https://doi.org/10.5281/zenodo.19697687)
- **Public Implementation Repository:** https://github.com/prakulhiremath/LOB-Latent-Regimes
- **Immutable Commit SHA:** `6bf8ec92632a1f0fd4d4be502d30ad7f2a7007ae`
- **Core Production Pipeline Script:** `Experiments/v7.py` (supported by `Experiments/v1.py` through `Experiments/v6.py`, `Results/summary.txt`, and `Notebook/LOB.ipynb`)

## Economic mechanism

### Source-reported

Conventional limit order book (LOB) early-warning indicators—such as order flow imbalance (OFI), short-term realized volatility spikes, and bid-ask spread widening—are inherently reactive. By construction, they trigger at time $\tau \ge \sigma$, where $\sigma$ is the observable onset of market stress. When volatility surges or spreads blow out, the stress event is already underway, leaving zero or negative lead-time ($\Delta = \sigma - \tau \le 0$) for risk mitigation.

The authors propose that liquidity stress events in electronic order books are not instantaneous step transitions, but rather the culmination of a latent deterioration phase ("build-up" phase). Grounded in microstructure theory (Kyle 1985; Bouchaud et al. 2009; Easley, López de Prado, and O'Hara 2012; Hasbrouck 1991), informed traders quietly accumulate positions or adverse selection builds up, leading liquidity providers to withdraw depth and widen quotes before aggressive market orders impact prices.

The data-generating process (DGP) is formulated as a three-state causal Markov chain $\{Z_t\}_{t \ge 1}$ on state space $\mathcal{Z} = \{0, 1, 2\}$:
1. **Regime 0 (Stable):** Tight bid-ask spread, high depth, low volatility, balanced order flow;
2. **Regime 1 (Latent Build-up):** Gradual depth erosion, subtle spread drift, mildly elevated imbalance—changes that individually remain submerged within stable-regime noise;
3. **Regime 2 (Stress):** Sharp spread blowout, depth collapse, elevated volatility, order-flow dislocation.

The transition probability matrix $\mathbf{P} \in [0, 1]^{3 \times 3}$ enforces the causal sequence $0 \to 1 \to 2$:
$$\mathbf{P} = \begin{pmatrix} p_{00} & p_{01} & 0 \\ 0 & p_{11} & p_{12} \\ p_{20} & 0 & p_{22} \end{pmatrix}$$
Transitions $0 \to 2$ (instantaneous stress without build-up) and $1 \to 0$ (recovery before stress) are disallowed in the base model, creating an expected prediction window of $\mathbb{E}[\text{dwell}_1] = 1 / p_{12}$. The latent regime sequence is proven identifiable up to label permutation from observable temporal drift (Theorem 1).

### Research interpretation

The hypothesized alpha and execution mechanism is **pre-stress liquidity void anticipation via hidden regime state-space modeling**. 

In high-frequency trading and market-making, the primary source of loss is adverse selection: quoting passively into an evaporating book right before a sharp market dislocation. A detector that reliably fires with positive lead-time ($\Delta > 0$) provides actionable edge in two distinct ways:
1. **Defensive Liquidity Provision (Alpha via Loss Avoidance):** Quoting engines can immediately cancel resting maker orders, widen quoting spreads, or pull bids/asks prior to the toxic sweep, preventing inventory toxicity and adverse fill cascades.
2. **Short-Horizon Directional Execution (Alpha via Toxic Flow Riding):** Aggressive execution algorithms can front-run impending liquidity collapse by lifting the remaining thin book before the spread widens, or temporarily withhold executions until the stress regime returns to equilibrium ($2 \to 0$).

The detection framework integrates four distinct feature channels through a **MAX-fusion trigger** paired with a **rising-edge filter**:
- **HMM Posterior Entropy ($S_t^{\text{ent}}$):** Captures state uncertainty. As the book enters build-up, posterior probability mass shifts between stable and build-up states, inflating entropy prior to regime certainty.
- **Depth Erosion ($S_t^{\text{dep}}$):** Captures structural withdrawal of liquidity providers across top-5 price levels.
- **Spread Drift ($S_t^{\text{spd}}$):** Tracks subtle slope increases in quoted spread normalized by volatility.
- **Order Flow Momentum ($S_t^{\text{ofi}}$):** Measures cumulative directional order flow toxicity.

**Component Roles in the Composite Detector:**
- *Primary Trigger (Structural Precursor):* Depth erosion ($S_t^{\text{dep}}$) accounts for 55.5% of first-trigger events in simulation and 100% of first-trigger events in BTC/USDT live data, validating that depth withdrawal causally precedes price impact.
- *Secondary Trigger (Regime Ambiguity):* HMM posterior entropy ($S_t^{\text{ent}}$) accounts for 44.4% of first-trigger events in simulation, firing as a confirmation within 10 seconds of depth erosion.
- *Filter / Aggregation Operator:* MAX aggregation selects the earliest signal breach across sparse channels without dilution from inactive channels.
- *Timing Gate:* The rising-edge condition ($S_t > S_{t-1}$) ensures the alert fires at the onset of deterioration rather than at the plateau or stress peak.

## Signal

### Signal Construction & Equations

1. **Feature Vector ($X_t \in \mathbb{R}^d$):** Constructed per 1-second bin:
   - Quoted spread: $A_t = 2 \cdot (\text{mid}_t - \text{bid}_t)$
   - Aggregate top-5 depth: $D_t = \sum_{k=1}^5 (V_{t,k}^{\text{bid}} + V_{t,k}^{\text{ask}})$
   - Order flow imbalance: $I_t = \frac{V_t^{\text{bid}} - V_t^{\text{ask}}}{V_t^{\text{bid}} + V_t^{\text{ask}} + 10^{-9}}$
   - Rolling return volatility: $\hat{\sigma}_t = \text{Std}(\Delta \ln(\text{mid}_{t-59:t}))$ over 60 seconds
   - Temporal derivatives: First differences $\Delta A_t, \Delta D_t$ smoothed with a 5-second Gaussian kernel

2. **Causal Preprocessing:**
   - Rolling z-score: Each feature is normalized using a causal 30-minute rolling mean and standard deviation: $Z_{t,j} = (X_{t,j} - \hat{\mu}_{t,j}^{(30\text{m})}) / \hat{\sigma}_{t,j}^{(30\text{m})}$.
   - Intraday Seasonality Removal: For real market data, remove deterministic hourly/diurnal patterns by subtracting day-of-week and hour-of-day medians estimated from the prior training window.

3. **Online Gaussian HMM Filtering:**
   - A 3-state Gaussian Hidden Markov Model with full covariance is fitted on a rolling 24-hour training window ($K=3$, Baum-Welch with 10 restarts).
   - Online forward filter computes causal state probabilities:
     $$\pi_t^{(k)} = \mathbb{P}(Z_t = k \mid X_{1:t}), \quad k \in \{0, 1, 2\}$$

4. **Channel Metric Generation:**
   - **(i) HMM Posterior Entropy:**
     $$S_t^{\text{ent}} = - \sum_{k=0}^2 \pi_t^{(k)} \log_2 \pi_t^{(k)}$$
   - **(ii) Temporal Depth Erosion:** Over rolling window $w = 60$ seconds:
     $$S_t^{\text{dep}} = \max\left(0, \frac{\bar{D}_w - D_t}{\bar{D}_w}\right) \cdot \mathbb{I}(\text{monotonic decay over } w)$$
   - **(iii) Spread Drift:**
     $$S_t^{\text{spd}} = \max\left(0, \frac{A_t - A_{t-w}}{\hat{\sigma}_A}\right)$$
   - **(iv) OFI Momentum:**
     $$S_t^{\text{ofi}} = \frac{1}{w} \left| \sum_{s=t-w+1}^t I_s \right|$$

5. **Composite Score & MAX Aggregation:**
   $$S_t = \max \left( S_t^{\text{ent}}, S_t^{\text{dep}}, S_t^{\text{spd}}, S_t^{\text{ofi}} \right)$$

6. **Rising-Edge Trigger Condition:**
   A trigger is emitted at timestep $t$ if and only if all three conditions are satisfied:
   1. $S_t > \theta_t$ (Score exceeds adaptive threshold);
   2. $S_t > S_{t-1}$ (Rising edge: score is actively accelerating upward, targeting build-up inflection);
   3. $t - \tau_{\text{last}} > L$ (Refractory spacing window: suppresses repeat alerts within $L = 20\text{–}60$ seconds).

7. **Adaptive Threshold Calibration:**
   $$\theta_t = \hat{F}_t^{-1}(p)$$
   where $\hat{F}_t$ is the empirical CDF of past composite scores $\{S_s\}_{s \le t}$ updated every 30 minutes, and $p = 0.85$ (85th percentile).

## Required data

- **Instrument:** Tested empirically on Binance BTC/USDT spot order book. Applicable to crypto perpetual futures and high-frequency equity limit order books (LOBSTER).
- **Venue:** Centralized exchange WebSocket feed (Binance public depth stream `@depth20@100ms`).
- **Timeframe:** 1 Hz (1-second aggregation bins constructed from raw 100 ms snapshots).
- **Depth Levels:** Top-5 levels aggregated for depth and OFI features; top-20 levels monitored.
- **Fields Required:** Best bid price, best ask price, bid volumes (levels 1–5), ask volumes (levels 1–5), trades in bin (taker buy volume, taker sell volume).
- **Point-in-Time Discipline:** Strictly causal. Rolling statistics use strictly past data ($[t-1800, t]$ for z-scores, $[t-60, t]$ for channel windows). HMM parameters are estimated exclusively on the preceding 24-hour training day; no test data enters model calibration.
- **Missing Data Handling:** Feed dropouts $\le 3$ bins forward-filled with last valid book; gaps $> 3$ seconds marked missing and filter reset. First 60 minutes of daily sessions excluded to purge boundary effects.

## Execution assumptions

- **Operational Role:** Early-warning risk overlay / quote cancellation signal for market makers, or entry filter for high-frequency momentum/stat-arb engines.
- **Latency Tolerance:** Sub-second to 5 seconds. Since the signal achieves an empirical lead-time of $+38 \pm 21$ seconds on BTC/USDT, algorithmic cancellation and hedging can execute comfortably within standard cloud/co-location latencies ($< 50$ ms).
- **Order Timing:** Evaluated at 1 Hz cadence.
- **Costs & Drag:** As a defensive overlay, transaction costs are asymmetric: the benefit is avoided toxic fills (often tens of basis points during spread blowouts of $6.8\times$ normal levels). If used for directional breakout taking, taker fees ($2\text{–}5$ bps) apply.

## Evidence

### Source-reported

All quantitative figures trace directly to Hiremath & Hiremath (2026), arXiv:2604.20949v1 (Sections 6.1–6.10, Section 9.5, Table 1, Table 2, Table 3, and `Results/summary.txt`):

#### 1. Synthetic Ground-Truth Simulation (200 Independent Runs, $T = 3000$ steps each)
- Parameters: $p_{01}=0.02, p_{12}=0.05, p_{20}=0.10$ (dwell times: 50 steps stable, 20 steps build-up, 10 steps stress); drift $\alpha = 0.03$, noise $\sigma_\varepsilon = 0.5$ (SNR $\approx 0.06$ per step):
  - **Adaptive Trigger (Proposed):**
    - Mean lead-time $\Delta = \sigma - \tau$: $+18.6 \pm 3.2$ timesteps (95% CI);
    - Precision: $1.00 \pm 0.00$ (100%—zero false starts during the latent phase);
    - Coverage: $0.54 \pm 0.06$ (52.6% in `summary.txt`, 54.0% across sweep);
    - Triggers emitted: $8.3 \pm 1.4$ per 3000 steps ($4.5 \pm 0.8$ matched early detections).
  - **HMM Posterior Thresholding Baseline:** Lead-time $+11.3 \pm 2.9$ timesteps; Precision $0.87 \pm 0.05$; Coverage 43.2%.
  - **CUSUM Baseline:** Lead-time $+2.1 \pm 1.8$ timesteps; Precision $0.43 \pm 0.08$.
  - **Order Flow Imbalance Baseline:** Lead-time $-4.2 \pm 1.1$ steps (up to $-24.8$ in summary.txt); Precision $0.549$; Coverage $78.7\%$.
  - **Realized Volatility Baseline:** Lead-time $-6.8 \pm 1.4$ steps (up to $-32.0$ in summary.txt); Precision $0.455$; Coverage $43.3\%$.
- **Channel Attribution Breakdown:** Depth erosion accounts for 55.5% of earliest trigger firings; HMM entropy accounts for 44.4%; spread drift and OFI contribute 0% of first triggers.
- **Ablation Study Results:**
  - Removing rising-edge condition ($S_t > S_{t-1}$): Precision collapses from $1.00$ to $0.71$ (fires at stress peaks rather than build-up onset).
  - Replacing MAX with SUM aggregation: Coverage drops from $0.54$ to $0.38$.
  - Fixed threshold vs adaptive: Fixed threshold precision degrades from $1.00$ to $0.93$.
  - Removing HMM entropy channel: Coverage drops from $0.54$ to $0.30$.

#### 2. Real High-Frequency BTC/USDT Binance Order Book Evaluation (1 Week, 1 Hz, 2.5M snapshots)
- 5 ground-truth labelled stress events (spread $\ge 3\times$ 10-minute median for $\ge 30$s; mean spread during events $= 6.8\times$ median):
  - **Adaptive Trigger:**
    - Total triggers emitted: 4;
    - Matched detections: 4 / 5;
    - False alarms: 0;
    - Precision: $4/4 = 1.00$ (100%);
    - Coverage: $4/5 = 0.80$ (80%);
    - Mean lead-time: $+38 \pm 21$ seconds (95% CI $[+5, +71]$ seconds).
  - **Baselines:**
    - Order flow imbalance: Mean lead-time $-8$ seconds (reactive);
    - Volatility threshold: Mean lead-time $-14$ seconds (reactive);
    - HMM posterior thresholding: Mean lead-time $+19 \pm 17$ seconds, Precision $0.67$ (2 false alarms out of 6 triggers).
  - **Channel Behavior:** In 100% (4/4) of real-data detections, depth erosion fired first, followed by HMM entropy within 10 seconds in 3 of 4 cases.

These results have not been independently reproduced.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Coverage Bound / Theoretical Trade-off (Proposition 3):** Higher lead-time requires triggering earlier in the build-up phase where the signal is weaker. In simulation, the aggregate missed detection rate was 46% (coverage 54%). Conditional analysis (Table 2) proves this is concentrated in low-SNR ($<0.15$), short build-up ($<10$ steps) regimes where coverage plummets to $0.03 \pm 0.02$.
- **Real-Data Missed Event Failure Mode:** 1 of 5 real stress events was completely missed. It occurred during an Asian-to-US session transition where ambient market depth opened $2.1\sigma_D$ below the prior day's training baseline. Because depth was already depressed, the depth erosion signal could not register further relative decay, and the low depth was absorbed into the HMM's noise variance, keeping the composite score below the 85th percentile threshold.
- **Structural Channel Correlation:** While MAX aggregation assumes weakly correlated channels under equilibrium, real-world order book depth, spread, and imbalance exhibit significant structural cross-correlation, attenuating the theoretical advantage of MAX over SUM in practice.
- **Small Real-World Sample:** Only 5 labelled stress events across 1 week of BTC/USDT data; standard deviations ($\pm 21$s) are wide relative to the mean ($+38$s), requiring cautious interpretation.

## Falsification plan

1. **Multi-Asset Cross-Validation:** Evaluate the identical detector across 10 high-liquidity cryptocurrency perpetual contracts (ETH, SOL, BNB, DOGE, XRP, AVAX, LINK, SUI, NEAR, PEPE) over $\ge 90$ days. **Failure rule:** If mean lead-time $\Delta \le 0$ on $\ge 3$ of the 10 assets, the claim that latent build-up precedes stress across liquid crypto books is falsified.
2. **Extended Sample Significance Test:** Run the pipeline on $\ge 6$ consecutive months of BTC/USDT and ETH/USDT order book data ($\ge 50$ labelled stress events). **Failure rule:** If out-of-sample precision falls below $0.70$ or empirical coverage falls below $0.35$, the detector cannot be considered a reliable operational early-warning tool.
3. **Exogenous Stress vs. Endogenous Stress Separation:** Test detector response on macro event shocks (e.g., FOMC rate releases, CPI prints) versus endogenous order book liquidity cascades. **Failure rule:** If lead-time for macro announcements is $\le 0$, the detector is confirmed to be an endogenous liquidity exhaustion detector only and incapable of anticipating exogenous information jumps.
4. **Economic P&L Proof via Simulation:** Embed the trigger into an automated market-making backtest as an order-cancellation overlay. **Failure rule:** If the reduction in adverse selection losses is smaller than the lost fee income from missed non-toxic spreads, the economic value of the early-warning signal is net-negative.

## Crypto portability

**Direct.**

The paper explicitly implements, tunes, and evaluates the complete pipeline on Binance BTC/USDT spot order book data at 1 Hz resolution using the Binance WebSocket depth feed.

**Crypto-Specific Microstructure Considerations:**
- **24/7 Continuous Session Shifts:** Unlike equities with distinct market open/close auctions, crypto trades continuously. However, liquidity regimes rotate sharply between Asian, European, and North American market hours. A static 24-hour HMM fit causes baseline miscalibration (the direct cause of the missed event in Section 9.5). Session-adaptive HMM retraining or rolling intraday baselines are mandatory.
- **WebSocket Feed Resilience:** Centralized exchange WebSocket feeds frequently drop packets or disconnect during extreme volume spikes (the exact moments when stress events occur). Robust feed reconnection and state caching are essential to prevent detector blind spots.
- **Tick Size & Fee Structure:** Binance BTC/USDT has a sub-basis-point tick size relative to mid-price ($< 5 \times 10^{-5}$), making spread drift subtle and placing the primary informational burden on multi-level depth erosion rather than spread alone.

## Limitations

- **Small Empirical Event Count:** The real-data evaluation spans only one week and 5 stress events ($n_\sigma = 5$). While simulation covers 200 runs and thousands of regimes, the real-world statistical power is limited.
- **Selective Coverage:** The 100% precision in both simulation and real data is achieved by setting a conservative 85th percentile threshold, which allows 46% of simulated events and 20% of real events to pass undetected.
- **Gaussian Emission Simplification:** The underlying HMM assumes Gaussian observation noise, whereas cryptocurrency order book features (especially spreads and volatility) exhibit extreme fat tails and skewness.
- **Stationarity Assumption in Daily Retraining:** Fitting the HMM once per 24 hours fails to track intra-day liquidity regime drifts, causing false negatives when baseline depth shifts between trading regions.
- **Execution Strategy Underspecification:** The paper formalizes the detection framework but does not simulate an end-to-end P&L execution strategy (e.g., optimal maker quote cancellation or taker breakout entry).

## Implementation status

Not implemented in our research stack. This is a source-captured research record of a peer-reviewed methodology and public implementation. No PyBroker, Nautilus, paper, testnet, or live trading verification has been conducted.

## Adoption boundary

This record is research material only. Its presence in this repository does not mean:
- profitable;
- validated alpha;
- approved for implementation;
- approved for paper trading;
- approved for testnet;
- approved for live trading.

The $+38$s lead-time and 100% precision are source-reported findings from an external study and public codebase; they do not constitute internal verification or an authorization to deploy capital.

## Related Wiki records

- [[quant/crypto-l2-liquidity-state-transitions-order-flow-2026-09-01]] — Examines state-dependent L2 liquidity transitions and order flow additivity in crypto futures; complementary to the latent build-up regime hypothesis.
- [[quant/crypto-perpetual-liquidation-cascade-early-warning-taker-flow-variance-2026-09-01]] — Analyzes variance compression in taker flow as an early warning for liquidation cascades; shares the pre-stress early-warning objective.
- [[quant/crypto-perpetual-lob-explainable-catboost-gmadl-microstructure-2026-09-01]] — Studies non-linear feature attribution in crypto perpetual LOB microstructure; provides complementary feature importance rankings.
- [[quant/clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03]] — Explores order flow imbalance clustering across microstructure states; relevant to the order flow momentum channel.
- [[quant/crypto-volume-synchronized-probability-of-toxicity-vpin-microstructure-2026-08-31]] — Measures flow toxicity; evaluated as a reactive baseline in Hiremath & Hiremath (2026).

## Sources

1. **Prakul Sunil Hiremath and Vruksha Arun Hiremath**, *"Early Detection of Latent Microstructure Regimes in Limit Order Books"*, arXiv preprint `arXiv:2604.20949v1 [cs.LG, q-fin.TR, stat.ME]`, submitted April 24, 2026; revised August 24, 2026.
   - Abstract URL: https://arxiv.org/abs/2604.20949
   - Full text HTML: https://arxiv.org/html/2604.20949v1
   - PDF: https://arxiv.org/pdf/2604.20949v1
2. **Prakul Sunil Hiremath and Vruksha Arun Hiremath**, *"Early Detection of Latent Micro-Regimes in Limit Order Books"*, Zenodo Archive, August 2026.
   - DOI: `10.5281/zenodo.19697687`
   - Stable URL: https://doi.org/10.5281/zenodo.19697687
3. **Prakul Sunil Hiremath**, *"LOB-Latent-Regimes: Latent Micro-Regimes in Limit Order Books: Identification and Early Detection"*, GitHub repository:
   - Repository URL: https://github.com/prakulhiremath/LOB-Latent-Regimes
   - Immutable Commit SHA: `6bf8ec92632a1f0fd4d4be502d30ad7f2a7007ae`
   - Exact implementation script: `Experiments/v7.py`
   - Baseline and ablation scripts: `Experiments/v1.py` through `Experiments/v6.py`
   - Empirical summary: `Results/summary.txt`
