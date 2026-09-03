---
schema: strategy-research-record-v1
title: "Endogenous Predatory Trading Cycles Under Square-Root Price Impact: A Hopf-Bifurcation Nonlinear Oscillator and Entropy-Reduction Framework"
created: 2026-09-03
updated: 2026-09-03
type: strategy-research-record
tags:
  - quant
  - strategy-research
  - source-backed
  - market-microstructure
  - predatory-trading
  - price-impact
  - square-root-law
  - hopf-bifurcation
  - limit-cycles
  - agent-based-model
  - cma-es
  - optimal-control
  - maxwells-demon
  - entropy-rate
status: research-only
confidence: medium
source_as_of: 2026-07-05
sources:
  - "https://arxiv.org/abs/2607.05141"
  - "https://doi.org/10.48550/arXiv.2607.05141"
  - "https://arxiv.org/html/2607.05141v1"
implementation_status: not-implemented
adoption: not-approved
approval_scope: research-only
contested: false
contradictions: []
---

# Endogenous Predatory Trading Cycles Under Square-Root Price Impact: A Hopf-Bifurcation Nonlinear Oscillator and Entropy-Reduction Framework

## Provenance

- **Primary paper:** Yang Zhou, Jianwen Chen, and Ruipeng Wei, *Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles in Learning-Agent Markets*, arXiv preprint `arXiv:2607.05141v1 [q-fin.CP, econ.EM, nlin.AO, physics.soc-ph, q-fin.TR]`, submitted 5 Jul 2026. DOI: `10.48550/arXiv.2607.05141`.
- **Author affiliations:** 
  - Yang Zhou: Institute of Natural Sciences, Westlake Institute for Advanced Study, and Department of Physics, School of Science and Research Center for Industries of the Future, Westlake University, Hangzhou, China (`zhouyang@westlake.edu.cn`).
  - Jianwen Chen: Greatwall Cigar Factory of China Tobacco Sichuan Industrial Co., Ltd., Sichuan, China.
  - Ruipeng Wei: Southwestern University of Finance and Economics, Chengdu, Sichuan, China.
- **Primary source text:** Complete author-published LaTeX source (`paper.tex`), bibtex references (`references.bib`), figures (`figs/`), and arXiv HTML5 experimental full text retrieved from `https://arxiv.org/src/2607.05141` and `https://arxiv.org/html/2607.05141v1` (July 2026 snapshot).
- **Public access URL:** https://arxiv.org/abs/2607.05141.
- **Source/data as-of:** 2026-07-05.
- **Source-identity deduplication:** Repository-wide audit confirmed zero matching records for `2607.05141`, `Yang Zhou`, `Ruipeng Wei`, `Hopf bifurcation`, `fold bifurcation`, or `Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles`. Existing predatory or manipulation research records in this repository address fundamentally distinct mechanisms:
  - `leveraged-etf-closing-rebalance-predatory-trading-reversal-2026-09-03.md` (arXiv:2608.03703) examines predatory front-running of deterministic end-of-day LETF mechanical flow.
  - `crypto-microstructure-complexity-measures-wash-trading-filter-2026-09-01.md` focuses on statistical filtering of wash trading in crypto order flow.
  - `market-making-online-lob-action-dependent-feedback-2026-09-02.md` investigates passive quoting feedback in limit order books.
  The Zhou, Chen, & Wei (2026) framework uniquely proves that sublinear (square-root) price impact is mathematically necessary to induce endogenous multi-cycle predatory trading limit cycles via a supercritical Hopf bifurcation, formalizing the four-phase cyclic policy as a Pontryagin bang-bang optimal control and proving an information-thermodynamic bound on extractable trading profit.

## Economic mechanism

### Source-reported

The paper investigates the endogenous emergence of multi-cycle predatory trading strategies in an agent-based financial market where an adaptive institutional investor interacts with $N_R = 20{,}000$ herding retail traders.

Key economic and physical principles established by the authors include:
1. **Four-Phase Manipulation Limit Cycle:** An institutional agent optimized by Covariance Matrix Adaptation Evolution Strategy (CMA-ES) spontaneously discovers a self-sustained multi-cycle predatory trading pattern without hard-coded rules. Each complete cycle comprises four distinct operational phases:
   - *Accumulation* ($\sim 26$ days): Aggressive net buying ($u \approx +0.88$) builds inventory while price impact is concave (sublinear).
   - *Push / Wash Trading* ($\sim 38$ days): Simultaneous buying and selling ($Q_{\mathrm{wash}} = \min(b_t, s_t) Q_{\max}$) drives price momentum upward through aggressive-side execution, igniting retail herding.
   - *Distribution* ($\sim 130$ days): Gradual net selling ($u < 0$, stealth factor $s = 0.5$) unloads inventory into incoming retail buying cascades.
   - *Reset* ($\sim 28$ days): Mean-reversion ($\mu = 0.01$) and retail drawdown panic selling ($\delta(P) = \min(0.25, |P/P_{\mathrm{peak}} - 1|)$) drive the asset price back to or below fundamental value $P_0$.
2. **Hopf Bifurcation and Capital Threshold:** By mapping the agent-based market to a two-dimensional autonomous mean-field ODE system in state $(x, q)$ (where $x = (P - P_0)/P_0$ is price deviation and $q$ is institutional holding fraction), the authors prove that the market undergoes a continuous supercritical Hopf bifurcation as institutional capital exceeds critical threshold $C_c$. The limit cycle oscillation amplitude scales as $A \propto (C - C_c)^\alpha$ with critical exponent $\alpha \approx 0.48$ (95% CI $[0.17, 0.64]$), consistent with the theoretical Hopf normal form $\alpha = 1/2$.
3. **Necessity of Square-Root Price Impact:** Square-root price impact $I(D) = \lambda \operatorname{sgn}(D) \sqrt{|D|/V_0}$ is mathematically essential. Because the derivative $\partial I / \partial D \propto |D|^{-1/2}$ diverges as $D \to 0$, sublinear impact provides the restoring nonlinearity that overcomes market damping at small order imbalances. In contrast, linear impact $I(D) \propto D$ eliminates the Hopf bifurcation entirely, rendering the retail market unconditionally stable.
4. **Herding-Independence ($\beta = 0$):** At calibrated herding scale $\mathrm{HS} = 10^{-3}$, the limit cycle persists even when retail herding is completely removed ($\beta = 0$): oscillation amplitude remains $x_{\mathrm{amp}} = 2.17\%$ (compared to $2.27\%$ at $\beta = 6$). The cycle is a self-sustained nonlinear oscillator created purely by position-tracking feedback coupled with concave market impact. When herding scale is elevated to $\mathrm{HS} = 10^{-2}$, a discontinuous fold (saddle-node) bifurcation appears, creating a first-order jump to zero amplitude.
5. **Maxwell's Demon Analogy and Entropy Reduction:** The institutional agent acts as an information-processing controller (Maxwell's demon) that observes behavioral noise fluctuations, opens/closes trading gates, and extracts profit while reducing the Shannon entropy rate of the market price process ($\Delta h = 0.016 \pm 0.011$ under LZ76, $p \approx 0.001$; $\Delta h_{\mathrm{MK}} = 0.0096 \pm 0.0032$ under first-order Markov, positive across all 20 seeds). Realized profit satisfies an information-thermodynamic upper bound derived from the Sagawa-Ueda equality: $\Pi \lesssim C_{\mathrm{SR}}(\beta) \times I(\mathbf{h}_t; r_{t+1}) \times T$.

### Research interpretation

From a quantitative strategy and market microstructure perspective, this research delivers two distinct, falsifiable alpha hypotheses:

1. **Active Institutional Predatory Execution Engine:** In illiquid, retail-dominated or segmented assets where price impact is concave (sublinear in order size), an institutional controller parameterized as a smooth feedback law $u = u_{\max} \tanh[g_q(q_t - q) + g_x x]$ (approximating Pontryagin bang-bang control) can systematically extract capital from price-insensitive, trend-chasing counterparties by inducing an artificial limit cycle, provided total available capital exceeds the critical Hopf threshold $C_c$.
2. **Defensive / Contrarian Regime-Phase Alpha (Nonlinear Cycle Exploitation):** For non-manipulating quantitative funds operating in markets vulnerable to cyclic manipulation (e.g., small-cap equities, meme coins, or low-float altcoins), understanding the $(q, x)$ phase-plane topology provides a predictive signal:
   - *Phase 1 Identification (Accumulation):* Institutional order flow increases while price deviation remains subdued ($x \approx 0$); ride long momentum alongside the accumulator.
   - *Phase 2 Identification (Push / Wash):* Daily volume surges ($V \gg V_0$) with simultaneous aggressive bid/ask crossing, accelerating 5-day return $r_{5d} > 0$ and driving retail participation to saturation ($p_{\mathrm{buy}} \to 1$).
   - *Phase 3 Warning (Distribution):* Price reaches peak overvaluation ($P/P_0 - 1 > \kappa_{\mathrm{ov}}^{-1}$), retail net flow is heavily positive, but institutional inventory begins declining ($u < 0$, stealth distribution); immediately exit longs and initiate directional short positions or purchase out-of-the-money puts.
   - *Phase 4 Reset (Cascade Exploitation):* Price breaks below the peak by $>5\%$, triggering the non-linear drawdown selling boost $\delta_{\mathrm{dd}}(P) = \min(0.25, |P/P_{\mathrm{peak}} - 1|)$; hold short until mean-reversion stabilizes near $P_0$ and retail volume collapses.

## Signal

The strategy logic can be deployed either as a direct cyclic controller or as a phase-detection signal that tracks the asset's position in the $(x, q)$ limit cycle.

### 1. Direct Bang-Bang / Smooth Feedback Controller (Systematic Execution Policy)

Under Pontryagin's maximum principle, the profit-maximizing institutional policy is piecewise constant (bang-bang) with switching boundaries on holding fraction $q$:
$$u_t^* = \begin{cases} +u_{\max}, & q_t < q_1 \quad (\text{Accumulate}) \\ 0 \text{ or wash}, & q_1 \le q_t \le q_2 \quad (\text{Push / Mark-up}) \\ -u_{\max}, & q_t > q_2 \quad (\text{Distribute}) \end{cases}$$

The smooth feedback parameterization implemented in the mean-field reduction:
$$u_t = u_{\max} \tanh\left[ g_q (q_t - q) + g_x x \right]$$
where:
- $u_t \equiv b_t - s_t \in [-1, 1]$: Net trading control.
- $q$: Current institutional holding fraction ($q \in [0, 1]$ of free float).
- $q_t$: Target holding fraction (calibrated optimal peak $q_t \approx 14.6\%$).
- $x = (P_t - P_0) / P_0$: Normalized price deviation from fundamental/anchor price.
- $g_q$: Feedback gain on holding deviation.
- $g_x$: Feedback gain on price deviation.

### 2. Observable Market Phase-Detection Signal (Contrarian / Cycle-Tracking Alpha)

For an external systematic trader observing publicly available market data (prices, volumes, order imbalances), the four cycle phases are classified as follows:

```text
Phase 1: Accumulation
  Trigger: x <= 0.02, r_5d < 0 or flat, positive institutional net accumulation proxy
  Action: Accumulate long / Enter trend-following long

Phase 2: Push / Markup
  Trigger: r_5d > 0.05, Volume > 1.5 * V_0, Bid-ask aggressor imbalance surging
  Action: Hold long with trailing stop; monitor for momentum exhaustion

Phase 3: Distribution
  Trigger: x > +0.15 (elevated deviation), Trend duration t_trend > tau_e (120 days),
           divergence between retail buying surge and flattening price
  Action: Close all long positions; enter short

Phase 4: Reset / Cascade
  Trigger: Price drops > 5% from cycle high P_peak (P <= 0.95 * P_peak),
           drawdown panic selling delta_dd active, high downside realized volatility
  Action: Maintain short until price deviation x approaches 0 (|x| <= 0.02)
```

- **Signal formation timestamp:** Daily close ($T+0$), actionable at next market open ($T+1$) or execution bar.
- **Lookback windows:**
  - Fast return window: $\tau_r = 5$ days ($r_{5d} = \sum_{s=0}^4 \Delta P_{t-s} / P_0$).
  - Trend exhaustion window: $\tau_e = 120$ days.
  - Drawdown peak window: Trailing rolling maximum over the current active cycle.
- **Position-sizing logic:** Fixed fractional capital allocation scaled to asset free float; institutional order capacity $Q = k_Q C$, capped at $Q_{\max} = N_{\mathrm{shares}} u_{\max} / 12$.

## Required data

- **Instrument:** Single liquid or semi-liquid equity or crypto perpetual contract with substantial retail participation.
- **Universe:** Assets exhibiting concave price impact (sublinear in order size, $|D|^{0.5}$), low to moderate institutional ownership, and high retail turnover.
- **Venues:** Centralized exchanges (equity exchanges with daily clearing like SSE/SZSE; crypto exchanges like Binance, Bybit, OKX; or decentralized order books).
- **Timeframe:** Daily bars (1D) for macro cycle identification; 1-minute to 1-hour intraday execution bars for order execution.
- **Required fields:**
  - Daily open, high, low, close (OHLCV).
  - Aggregate trading volume ($V_t$) and baseline volume benchmark ($V_0$).
  - Estimated net buyer-initiated volume / aggressor trade imbalance.
  - Fundamental anchor or moving median price ($P_0$).
  - Cycle peak price tracker ($P_{\mathrm{peak}}$).
- **Point-in-time constraints:** All features ($r_{5d}$, $P_{\mathrm{peak}}$, cumulative volume, drawdown depth) must be computed strictly point-in-time without look-ahead bias.

## Execution assumptions

- **Price impact model:** Square-root impact $\frac{\Delta P}{P} = \lambda \operatorname{sgn}(D_{\mathrm{net}}) \sqrt{\frac{|D_{\mathrm{net}}|}{V_0}}$ with calibrated impact parameter $\lambda = 0.008$.
- **Base volume:** $V_0$ representing normal daily market liquidity.
- **Settlement & constraints:**
  - Primary paper incorporates Chinese A-share rules: daily price limits ($\pm 10\%$), $T+1$ settlement restriction, and stealth distribution ($s = 0.5$).
  - Ablation experiments prove that the cycle survives completely with or without price limits, with or without wash trading, and with or without stealth distribution (return variation $< 3\%$).
- **Order types:** Aggressive market orders or aggressive limit orders during push phase; passive iceberg or TWAP/VWAP orders during accumulation and distribution.
- **Transaction costs:** Standard maker/taker fees, exchange clearing fees, and stamp duties. In equity markets, round-trip costs $\sim 10\text{--}20\text{ bps}$; in crypto perps, maker $\sim 0\text{--}2\text{ bps}$, taker $\sim 4\text{--}5\text{ bps}$.

## Evidence

### Source-reported

All empirical figures below are transcribed directly from Zhou, Chen, & Wei (2026), based on their agent-based simulation and mean-field bifurcation analysis:

1. **Cycle Formation and Overall Performance (Table I, Table \ref{tab:baseline}, Table \ref{tab:episode_length}):**
   - Over $T = 2000$ trading days across 20 independent evaluation seeds (seeds 42–61):
     - Complete cycle count: 8 to 11 cycles (mean: 9 cycles; period $T \approx 222$ days).
     - Best individual seed portfolio return: $+51\%$.
     - 20-seed mean portfolio return: $+37.7 \pm 5.2\%$ (all 20 seeds positive).
     - 20-seed mean PnL: $+43.8 \pm 3.4\%$.
     - Re-evaluation under fixed parameters (Table I): $+36.7 \pm 3.6\%$ return, $+44.3 \pm 4.3\%$ PnL, 9.0 cycles.
2. **Four-Phase Timing and ODE Calibration (Table \ref{tab:prediction}):**
   - Accumulation duration: predicted 28 days, observed 26 days (error $< 10\%$).
   - Push / wash-trading duration: observed $\sim 38$ days.
   - Distribution duration: predicted 57 days (with $S = 0.5$), observed 130 days (difference driven by gradual multi-day position unwinding).
   - Reset duration: observed $\sim 28$ days.
   - Total cycle period: predicted $150\text{--}200$ days, observed 222 days.
   - Peak institutional holding $q_{\max}$: predicted $14.5\%$, observed $14.6\%$.
   - Institutional impact derivative $\kappa_\varepsilon$: predicted 0.004, observed 0.004.
   - Herding coupling $C_{\mathrm{SR}}$: predicted 0.011, observed 0.011.
   - Mean-field SDE correlation with agent simulation: $r = 0.62$.
3. **Bifurcation Characteristics:**
   - Analytical Hopf boundary: $C_c = 1.57\%$ at $\lambda = 0.008$.
   - Numerical Hopf boundary (binary search): $C_c^{\mathrm{num}} = 1.31\%$ (agreement within $20\%$).
   - Critical scaling exponent: $A(C) \propto (C - C_c)^\alpha$ with $\alpha \approx 0.48$ (bootstrap 95% CI $[0.17, 0.64]$), consistent with the standard Hopf prediction $\alpha = 1/2$.
   - Robustness to noise-floor regularization $\varepsilon \in [3\times 10^4, 3\times 10^5]$: exponent $\alpha \in [0.41, 0.48]$.
   - Linear impact baseline: Linear impact $I(D) = \lambda D / V_0$ completely eliminates the Hopf bifurcation; damping $\Gamma(v_0) = \mu + 1/\tau_r - C_{\mathrm{SR}}/\sqrt{v_0} > 0$ remains strictly positive for all $v_0$ and $\beta$, making the retail market unconditionally stable.
4. **Baseline Strategy Comparisons across 20 Seeds (Table \ref{tab:baseline}):**
   - **LSTM (Proposed):** Return $+37.7 \pm 5.2\%$, PnL $+43.8 \pm 3.4\%$, Cycles: 9.
   - **Buy-and-Hold:** Return $-33.4 \pm 3.6\%$, PnL $0.0\%$, Cycles: 0 (fails due to mean-reverting fundamentals).
   - **Hold:** Return $0.0\%$, PnL $0.0\%$, Cycles: 0.
   - **Threshold Rule ($r_{5d} < -0.05$ buy, $> 0.10$ sell):** Return $-0.6 \pm 0.6\%$, PnL $0.0\%$, Cycles: 0.
   - **Momentum Rule (linear in $r_{5d}$):** Return $-3.9 \pm 3.1\%$, PnL $+0.8 \pm 1.5\%$, Cycles: 0.
   - **Contrarian Rule (dips buy, rallies sell):** Return $-1.6 \pm 1.9\%$, PnL $+2.0 \pm 1.2\%$, Cycles: 0.1.
5. **Architecture and Reward Independence (Appendices S7 & S13):**
   - **2-Layer MLP (162 parameters):** Replacing the 530-parameter LSTM with a simple feedforward MLP achieves mean return $+50\%$ across 20 seeds (vs. $+40\%$ for LSTM under identical 200-generation training budget), reproducing identical 4-phase cyclic limit cycles and proving the phenomenon is driven by market microstructure rather than recurrent architecture.
   - **Terminal return only:** Retraining without cycle bonus yields $+51\%$ return across 20 seeds (vs. $+43\%$).
6. **Mechanism Ablation (Table I):**
   - Full model: $+36.7 \pm 3.6\%$ return, 9.0 cycles.
   - No wash trading impact: $+39.7 \pm 4.4\%$ return, 7.7 cycles (wash trading increases cycle frequency at slight cost to per-cycle efficiency).
   - No daily price limits: $+37.6 \pm 3.6\%$ return, 8.7 cycles.
   - No stealth distribution ($s = 1.0$): $+37.1 \pm 5.5\%$ return, 8.8 cycles.
7. **Entropy Reduction & Information-Thermodynamic Bound (Table \ref{tab:info_bound}, Appendices S4 & S11):**
   - Normalized Lempel-Ziv (LZ76) entropy rate: reduced from $h_{\mathrm{retail}} = 0.988 \pm 0.009$ to $h_{\mathrm{inst}} = 0.972 \pm 0.006$ ($\Delta h = 0.016 \pm 0.011$, 17/20 seeds positive, $p \approx 0.001$; Wilcoxon signed-rank $p < 0.01$).
   - First-order Markov conditional entropy: $\Delta h_{\mathrm{MK}} = 0.0096 \pm 0.0032$, positive in 20/20 seeds.
   - Permutation entropy: $\Delta h_{\mathrm{PE}} = 0.0001 \pm 0.0006$ (ordinal patterns unchanged; amplitude distribution regularized).
   - Sagawa-Ueda bound $\Pi \le C_{\mathrm{SR}} \times I(\mathbf{h}_t; r_{t+1}) \times T$: Return-to-bound ratio ranges from 0.090 to 0.320 across $\beta \in [2, 12]$, satisfying the bound with a 3--10$\times$ margin.
8. **Capital Sweep (Appendix S8):**
   - Best fitness: $C = 1\% \to +168\%$; $C = 2\% \to +312\%$; $C = 5\% \to +222\%$; $C = 10\% \to +128\%$. Non-monotonicity reflects self-induced market impact at high capital.

### Independently reproduced

Not independently reproduced.

### Negative evidence

- **Retail-Only Inability to Self-Oscillate:** The paper mathematically proves that retail herding alone cannot create sustained price cycles under square-root price impact. Damping $\Gamma(v_0)$ is strictly positive across all tested $\beta \in [2, 12]$ and return variances $v_0$. Retail markets without an active strategic manipulator are stable focuses.
- **Failure Under Linear Price Impact:** If price impact is linear ($I \propto D$), the Hopf bifurcation vanishes. A predatory agent cannot sustain a profitable limit cycle because linear impact lacks the concave restoring force that makes accumulation cheap and distribution profitable.
- **Complete Failure of Classical Rule-Based Strategies:** Fixed technical rules (Momentum $-3.9\%$, Contrarian $-1.6\%$, Threshold $-0.6\%$, Buy-and-Hold $-33.4\%$) fail completely in this environment because static rules lack the state memory and phase-dependent switching required to coordinate accumulation and distribution.
- **Non-Monotonic Capital Scaling:** Strategy profitability peaks at intermediate capital ($C = 2\%$) and decays at larger capital levels ($C = 5\%, 10\%$) due to severe self-induced market impact during inventory liquidation.
- **Diminishing Returns in Extended Horizons:** Over $T = 4000$ days, per-cycle profit gradually decays due to the depletion of retail liquidity/wealth within a closed market pool.

## Falsification plan

To falsify the existence of the limit cycle or its exploitation as an alpha signal, the following empirical and simulation tests are formulated:

1. **Price Impact Linearity Test:** Measure the empirical price impact function $I(D)$ across target asset classes. If the price impact is strictly linear or convex ($\partial^2 I / \partial D^2 \ge 0$) rather than concave ($\partial^2 I / \partial D^2 < 0$), the Hopf bifurcation is eliminated. Failure criterion: Impact exponent $\gamma$ in $I(D) \propto D^\gamma$ satisfies $\gamma \ge 1.0$ ($p < 0.05$).
2. **Capital Threshold Test ($C < C_c$):** Deploy the policy in an agent-based simulation with institutional capital held below $C_c \approx 1.31\%$. Failure criterion: Persistent limit cycles (amplitude $A > 0$) emerge below $C_c$, which would contradict the supercritical Hopf bifurcation characterization.
3. **Competing Strategic Agents (Multi-Demon Ablation):** Introduce two or more independent CMA-ES / RL institutional agents into the same market. If competing agents cannibalize each other's accumulation or front-run the distribution phase, the limit cycle collapses into chaotic dissipation. Failure criterion: Realized portfolio return drops below zero when institutional agent count $N_{\mathrm{inst}} \ge 2$.
4. **Phase-Space Cycle Predictability Test in Historical Data:** On a historical universe of micro-cap stocks or low-liquidity altcoins, fit the phase-space trajectory $(x, q)$ using rolling volume and price deviation. Failure criterion: Out-of-sample directional predictability in Phase 3 (shorting into distribution) achieves an Information Coefficient (IC) statistically indistinguishable from zero ($t$-stat $< 1.96$).
5. **Entropy-Rate Placebo Test:** Compute the LZ76 and Markov-1 entropy rates on trade-time return series. Failure criterion: Shuffling order arrival times or removing institutional trade markers fails to increase the estimated entropy rate ($\Delta h \le 0$).

## Crypto portability

**Portability Classification: Adapted / Unproven.**

The core mathematical mechanism originates from a stylized agent-based model with Chinese A-share institutional settings ($\pm 10\%$ price limits, $T+1$ settlement, stealth distribution factor). While the authors proved that these market rules shape but do not create the cycles, porting the strategy to cryptocurrency markets requires substantial adaptation and remains unproven:

1. **Continuous 24/7 Trading & Absence of Price Limits:** Crypto markets operate 24/7 without daily closing auctions, circuit breakers, or $\pm 10\%$ price limits. While ablation experiments (Table I) show that removing price limits preserves profitability ($+37.6 \pm 3.6\%$), the absence of bounds allows flash crashes and runaway liquidation cascades that can distort the smooth reset phase.
2. **Perpetual Futures Funding Rate Drag:** In crypto perpetual futures, accumulating a dominant long position ($q \approx 14.6\%$ of open interest) pushes the perpetual price above the index, driving the funding rate heavily positive. Holding long inventory during the accumulation and push phases incurs substantial funding rate payments to short counterparties, eroding the spread capture.
3. **Dual Price Architecture (Mark vs. Index Price):** Perpetual futures liquidations and margin calls are triggered by the mark price (derived from external spot index prices), not the local last-traded price. Internal wash trading on a single perp venue cannot trigger index-driven liquidation cascades unless the spot reference index is manipulated across multiple liquid venues.
4. **Front-Running and MEV on Decentralized Exchanges:** On AMMs or decentralized order books, institutional accumulation and distribution are vulnerable to MEV searchers (sandwich attacks, JIT liquidity extraction), which front-run large trades and amplify execution costs far beyond classical centralized models.
5. **Retail Herding Dynamics in Altcoins / Meme Tokens:** Meme coins and low-cap altcoins exhibit extreme retail herding ($\beta \gg 6$) and social-media-driven momentum cascades. While the mechanism naturally fits this behavioral archetype, extreme liquidity fragmentation and token rug-pull risks present major operational challenges.

## Limitations

- **Single-Asset Closed Economy:** The model examines a single asset with a closed pool of 20,000 retail agents, neglecting cross-asset capital flows, sector rotation, and broader macroeconomic drivers.
- **Single Institutional Monopolist:** Only one strategic agent is simulated. Real markets contain multiple competing quantitative funds, market makers, and institutional allocators whose interactions may prevent the formation of clean periodic limit cycles.
- **Stylized Execution vs. Full Limit Order Book:** Clearing occurs via daily aggregate net demand and square-root impact rather than queue-level limit order book dynamics, omitting bid-ask spread crossing, order cancellation queues, and microsecond latency.
- **Absence of Real Historical Backtest:** All performance numbers ($+37.7\%$ mean return, 9 cycles over 2000 days) are source-reported from an agent-based computational market simulation and mean-field ODE solution, not an audited historical trading track record.
- **Unproven in Crypto Perpetuals:** While theoretically portable to high-herding altcoins, the strategy has not been validated on cryptocurrency data.

## Implementation status

- `implementation_status: not-implemented`
- This record represents an upstream theoretical and agent-based research capture only.
- No implementation has been created in PyBroker, NautilusTrader, paper trading, testnet, or live trading systems.

## Adoption boundary

- `status: research-only`
- `adoption: not-approved`
- `approval_scope: research-only`
- Research capture does not constitute investment advice, quantitative validation, or authorization to trade. Any future consideration requires extensive multi-agent simulation, transaction cost modeling, and empirical validation.

## Related Wiki records

- `[[quant/leveraged-etf-closing-rebalance-predatory-trading-reversal-2026-09-03]]`
- `[[quant/crypto-microstructure-complexity-measures-wash-trading-filter-2026-09-01]]`
- `[[quant/market-making-online-lob-action-dependent-feedback-2026-09-02]]`
- `[[quant/clusterlob-order-flow-imbalance-trader-behavior-clustering-2026-09-03]]`
- `[[quant/market-making-axiomatic-unified-inventory-quoting-spread-decomposition-2026-09-02]]`

## Sources

- **Primary paper:** Yang Zhou, Jianwen Chen, and Ruipeng Wei, *Square-Root Price Impact Is Necessary for Endogenous Manipulation Cycles in Learning-Agent Markets*, arXiv preprint `arXiv:2607.05141v1 [q-fin.CP, econ.EM, nlin.AO, physics.soc-ph, q-fin.TR]`, submitted 5 Jul 2026. DOI: `10.48550/arXiv.2607.05141`.
  - Abstract & metadata: https://arxiv.org/abs/2607.05141
  - Full text HTML: https://arxiv.org/html/2607.05141v1
  - TeX source archive: https://arxiv.org/src/2607.05141
- **Foundational literature cited within primary source:**
  - R. Almgren, C. Thum, E. Hauptmann, and H. Li (2005), *Direct estimation of equity market impact*, Risk 18 (7), 57–62.
  - J. Donier, J. Bonart, I. Mastromatteo, and J. Bouchaud (2015), *A fully consistent, minimal model for non-linear market impact*, Quantitative Finance 15 (7), 1109–1121.
  - F. Bucci, M. Benzaquen, F. Lillo, and J. Bouchaud (2019), *Crossover from linear to square-root market impact*, Physical Review Letters 122 (10), 108302.
  - G. Maitrier, G. Loeper, K. Kanazawa, and J. Bouchaud (2026), *The “double” square-root law: evidence for the mechanical origin of market impact using Tokyo stock exchange data*, Quantitative Finance 26, 491–503.
  - M. K. Brunnermeier and L. H. Pedersen (2005), *Predatory trading*, The Journal of Finance 60 (4), 1825–1863.
  - T. Lux and M. Marchesi (1999), *Scaling and criticality in a stochastic multi-agent model of a financial market*, Nature 397 (6719), 498–500.
  - N. Hansen and A. Ostermeier (2001), *Completely derandomized self-adaptation in evolution strategies*, Evolutionary Computation 9 (2), 159–195.
  - T. Sagawa and M. Ueda (2010), *Generalized Jarzynski equality under measurement and feedback control*, Physical Review Letters 104 (9), 090602.
  - T. Sagawa and M. Ueda (2012), *Nonequilibrium thermodynamics of feedback control*, Physical Review E 85 (2), 021104.
  - A. Lempel and J. Ziv (1976), *On the complexity of finite sequences*, IEEE Transactions on Information Theory 22 (1), 75–81.
